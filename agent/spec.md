## Agent Role
The agent acts as an autonomous neuroscience researcher.

## Allowed Actions
The agent may:
- Propose an experiment configuration
- Call preprocessing, training, and evaluation tools
- Inspect metrics
- Decide whether to modify or stop

## Forbidden Actions
The agent may NOT:
- Write or modify code
- Access the internet
- Assume results without running tools

## Success Criteria
An experiment is successful if:
- Evaluation completes without error
- Metrics are logged
- The agent can justify next steps

This prevents Gemini chaos later.

5️⃣ Only AFTER spec → write first real code

Your FIRST real Python file (tomorrow / next 2–3 hours)

Create: tools/run_experiment.py

This file must:
- Take a config dict
- Run ONE experiment
- Return metrics
- No Gemini here. No Streamlit.

Skeleton (write this, don't overthink):

```python
def run_experiment(config):
    """
    config: dict with keys
      - model
      - dataset
      - epochs
      - learning_rate
      - evaluation
    """
    print(f"Running experiment: {config}")
    
    # TODO:
    # 1. Load dataset
    # 2. Preprocess
    # 3. Train model
    # 4. Evaluate
    # 5. Return metrics
    
    metrics = {
        "accuracy": None,
        "auc": None,
        "notes": "placeholder"
    }
    return metrics
```

This is your control surface.

6️⃣ app.py — DO NOT TOUCH YET 🚫

I know Kiro auto-generated Streamlit scaffolding. Ignore it for now.

Why?
- UI too early = distraction
- Judges don't care about UI polish
- Agent must work headless first

We will come back to app.py after the agent can run 2 iterations autonomously.

7️⃣ Where Gemini comes in (NOT YET)

Gemini should be added only when:
- run_experiment(config) works
- You can run it manually with 2 configs
- Metrics are reproducible

Otherwise Gemini will amplify bugs.