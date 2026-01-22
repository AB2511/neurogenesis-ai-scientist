from agent.agent import call_gemini
from agent.prompts import PLANNER_PROMPT, CRITIC_PROMPT
from tools.run_experiment import run_experiment
import json

def run_autonomous_loop():
    # Load memory
    with open("agent/memory.json") as f:
        memory = json.load(f)
    
    # PLAN
    plan = call_gemini(PLANNER_PROMPT.format(
        goal=memory["goal"],
        history=memory["history"]
    ))
    
    # RUN
    metrics = run_experiment(plan)
    
    # CRITIQUE
    critique = call_gemini(CRITIC_PROMPT.format(
        goal=memory["goal"],
        experiment=plan,
        metrics=metrics
    ))
    
    # SCIENTIFIC STOPPING LOGIC
    if len(memory["history"]) >= 1:
        last_accuracy = memory["history"][-1]["metrics"]["within_subject_accuracy"]
        current_accuracy = metrics["within_subject_accuracy"]
        
        # If no improvement after parameter changes, force stop
        if abs(last_accuracy - current_accuracy) < 0.001:  # No meaningful change
            critique["decision"] = "stop"
            critique["analysis"] = "No measurable improvement across parameter changes. Performance appears to have reached a ceiling with current feature extraction and model architecture. Further hyperparameter tuning is unlikely to yield significant gains. Terminating exploration."
            print("\n🔬 SCIENTIFIC JUDGMENT: Forced stop due to performance plateau")
    
    # SAVE MEMORY
    memory["history"].append({
        "experiment": plan,
        "metrics": metrics,
        "analysis": critique
    })
    
    with open("agent/memory.json", "w") as f:
        json.dump(memory, f, indent=2)
    
    return plan, metrics, critique

if __name__ == "__main__":
    plan, metrics, critique = run_autonomous_loop()
    print("Plan:", json.dumps(plan, indent=2))
    print("Metrics:", json.dumps(metrics, indent=2))
    print("Critique:", json.dumps(critique, indent=2))
    
    if critique["decision"] == "stop":
        print("\n🏁 AGENT DECISION: STOP - Scientific exploration complete")