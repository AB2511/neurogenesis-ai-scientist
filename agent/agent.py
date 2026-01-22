import json
import os
from dotenv import load_dotenv
import google.generativeai as genai
from agent.prompts import SYSTEM_PROMPT, PLANNER_PROMPT, CRITIC_PROMPT

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

def call_gemini(prompt):
    response = model.generate_content(prompt)
    text = response.text.strip()
    
    # Remove markdown code blocks if present
    if text.startswith("```json"):
        text = text[7:]  # Remove ```json
    if text.endswith("```"):
        text = text[:-3]  # Remove ```
    
    text = text.strip()
    return json.loads(text)