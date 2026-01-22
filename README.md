# Neurogenesis AI Scientist

Neurogenesis AI Scientist is an autonomous AI agent that designs, executes, evaluates, and critiques neuroscience experiments using real EEG data — demonstrating AI-for-Science through independent scientific reasoning rather than metric chasing.

## 🧠 What This Is

This is not just another EEG classifier. This is an **autonomous neuroscientist** that:

- **Plans experiments** using Gemini AI
- **Executes real EEG analysis** on 20 subjects
- **Critiques results** scientifically  
- **Refines experimental hypotheses** autonomously
- **Maintains scientific memory** across experiments

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Clone and navigate
cd neurogenesis-ai-scientist

# Install dependencies
pip install -r requirements.txt

# Setup API key
cp .env.example .env
# Edit .env and add your Gemini API key
```

### 2. Prepare Data

```bash
# Extract EEG data
python tools/prepare_dataset.py

# Verify data integrity
python tools/check_dataset.py
```

### 3. Run Autonomous Agent

```bash
# Single autonomous iteration
python app.py
```

## 🏗️ Architecture

```
Goal (text) 
    ↓ 
Gemini Planner → experiment_config.json 
    ↓ 
run_experiment(config) 
    ↓ 
metrics.json 
    ↓ 
Gemini Critic (reflection) 
    ↓ 
Revised config OR stop
```

## 📁 Project Structure

```
neurogenesis-ai-scientist/
├── agent/
│   ├── spec.md           # Agent specifications
│   ├── prompts.py        # Gemini prompts
│   ├── agent.py          # Gemini integration
│   └── memory.json       # Persistent scientific memory
├── tools/
│   ├── prepare_dataset.py    # Data extraction
│   ├── check_dataset.py      # Data validation
│   ├── epoch_p300.py         # EEG preprocessing
│   └── run_experiment.py     # Experiment engine
├── data/
│   ├── sub-001.zip → sub-020.zip  # Raw EEG data
│   └── erp_core/                  # Extracted data
└── app.py                # Autonomous loop
```

## 🔬 Scientific Approach

### Phase 1: Deterministic Experiment Engine
- Pure, reproducible EEG pipeline
- P300 event detection and epoching
- Within-subject classification
- Deterministic results (69.6% baseline accuracy)

### Phase 2: Autonomous Agent
- Gemini plans experiments based on previous results
- Real EEG experiments on 20 subjects  
- Scientific critique and hypothesis formation
- Autonomous iteration with justified stopping criteria

## 🎯 For Judges

This demonstrates **AI-for-Science** in action:

- **Not**: "Here's my EEG accuracy"
- **Yes**: "Here's an AI agent that autonomously designs and evaluates neuroscience experiments"

The agent shows:
- Scientific hypothesis formation
- Experimental design reasoning
- Result interpretation
- Methodological refinement
- Justified decision making

## 🔧 Technical Details

- **EEG Data**: 20 subjects, P300 oddball paradigm
- **Preprocessing**: MNE-Python, 0-600ms epochs, baseline correction
- **Classification**: Logistic regression on flattened features
- **Evaluation**: Within-subject train/test split
- **AI Agent**: Gemini 2.5 Flash with structured prompts

## 📊 Example Results

```json
{
  "experiment_id": "exp_001",
  "model": "LogisticRegression", 
  "max_iter": 1000,
  "regularization": 0.01,
  "evaluation": "within_subject",
  "reasoning": "Establishing baseline performance..."
}
```

**Metrics**: 69.6% accuracy
**Agent Decision**: Continue with modified parameters
**Scientific Reasoning**: "Regularization may need adjustment for better generalization..."

## 🛡️ Security

- API keys stored in `.env` (not committed)
- Environment variables loaded via `python-dotenv`
- `.gitignore` protects sensitive files

## 📝 License

MIT License - See LICENSE file for details.