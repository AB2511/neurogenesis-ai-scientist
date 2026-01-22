import mne
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from tools.epoch_p300 import epoch_p300

DATA_ROOT = Path("data/erp_core")

REQUIRED_KEYS = {
    "experiment_id",
    "model",
    "max_iter",
    "regularization",
    "evaluation"
}

def validate_config(config):
    missing = REQUIRED_KEYS - set(config.keys())
    if missing:
        raise ValueError(f"Missing config keys: {missing}")

def load_all_subjects():
    subjects = sorted(DATA_ROOT.glob("sub-*"))
    raws = []
    
    for sub in subjects:
        eeg_dir = sub / "eeg"
        eeg_file = list(eeg_dir.glob("*.set"))[0]
        raw = mne.io.read_raw_eeglab(eeg_file, preload=True, verbose=False)
        raws.append((sub.name, raw))
    
    return raws

def evaluate_within_subject(X, y, config):
    accs = []
    
    for i in range(len(X)):
        Xi, yi = X[i], y[i]
        Xtr, Xte, ytr, yte = train_test_split(
            Xi, yi, test_size=0.3, random_state=42
        )
        
        model = train_simple_classifier(
            Xtr, ytr, 
            max_iter=config.get('max_iter', 1000),
            regularization=config.get('regularization', 0.01)
        )
        ypred = model.predict(Xte)
        accs.append(accuracy_score(yte, ypred))
    
    return float(np.mean(accs))

def train_simple_classifier(X, y, max_iter=1000, regularization=0.01):
    # Flatten features for logistic regression
    X_flat = X.reshape(X.shape[0], -1)
    model = LogisticRegression(
        random_state=42, 
        max_iter=max_iter,
        C=1.0/regularization  # C is inverse of regularization
    )
    model.fit(X_flat, y)
    
    # Return a wrapper that handles flattening for prediction
    class FlattenWrapper:
        def __init__(self, model):
            self.model = model
        
        def predict(self, X):
            X_flat = X.reshape(X.shape[0], -1)
            return self.model.predict(X_flat)
    
    return FlattenWrapper(model)

def run_experiment(config):
    """
    config: dict with keys
      - experiment_id
      - model
      - max_iter
      - regularization
      - evaluation
    """
    print(f"Running experiment: {config}")
    
    validate_config(config)
    raws = load_all_subjects()
    
    X_all, y_all, subjects = [], [], []
    
    for sid, raw in raws:
        X, y = epoch_p300(raw)
        X_all.append(X)
        y_all.append(y)
        subjects.extend([sid] * len(y))
    
    # Evaluate within-subject
    acc = evaluate_within_subject(X_all, y_all, config)
    
    metrics = {
        "within_subject_accuracy": acc,
        "notes": "logistic_regression_baseline"
    }
    
    return metrics