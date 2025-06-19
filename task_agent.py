import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def read_tasks(filepath):
    with open(filepath, "r") as f:
        return f.read()

def summarize_tasks(tasks):
    prompt = f"""
You are a smart task planning agent.
Given a list of tasks, categorize them into 3 priority buckets:
- High Priority
- Medium Priority
- Low Priority

Tasks:
{tasks}

Return the response in this format:

High Priority:
- task 1

Medium Priority:
- task 1

Low Priority:
- task 1
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    task_text = read_tasks("tasks.txt")
    summary = summarize_tasks(task_text)
    print("\nTask Summary\n" + "-" * 30)
    print(summary)

