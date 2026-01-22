import mne
import numpy as np

def epoch_p300(raw):
    """
    Returns:
        X: np.ndarray [n_epochs, n_channels, n_times]
        y: np.ndarray [n_epochs]
    """
    
    # Standard ERP-CORE P3 events
    events, event_id = mne.events_from_annotations(raw)
    
    # ERP-CORE P3 convention: 
    # Target stimuli typically have codes ending in 1 or 2
    # Non-target stimuli typically have codes ending in 3, 4, 5
    target_codes = []
    nontarget_codes = []
    
    for code_str in event_id.keys():
        code = str(code_str)
        if code.endswith('1') or code.endswith('2'):
            target_codes.append(event_id[code_str])
        elif code.endswith('3') or code.endswith('4') or code.endswith('5'):
            nontarget_codes.append(event_id[code_str])
    
    if not target_codes or not nontarget_codes:
        raise RuntimeError(f"Could not find P3 target/nontarget events. Available: {list(event_id.keys())}")
    
    # Create event mapping - include all relevant codes
    event_map = {}
    for i, code in enumerate(target_codes):
        event_map[f'target_{i}'] = code
    for i, code in enumerate(nontarget_codes):
        event_map[f'nontarget_{i}'] = code
    
    epochs = mne.Epochs(
        raw,
        events,
        event_id=event_map,
        tmin=0.0,
        tmax=0.6,
        baseline=(0.0, 0.1),
        preload=True,
        verbose=False
    )
    
    X = epochs.get_data()
    y = epochs.events[:, -1]
    
    # Convert event codes to binary labels
    y_binary = np.zeros(len(y))
    for i, event_code in enumerate(y):
        if event_code in target_codes:
            y_binary[i] = 1
        else:
            y_binary[i] = 0
    
    return X, y_binary.astype(int)