import requests
import os

OLLAMA_URL = os.getenv("OLLAMA_URL")  # Get OLLAMA URL from environment variable or use default
MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:1b")  # Get model name from environment variable or use default

def replying_input(preprompt, prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt" : f"{preprompt}\n{prompt}",
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to OLLAMA server: {e}")
        return None
    response = response.json()
    return response.get("response").strip()

if __name__ == "__main__":
    preprompt = "Only reply in Vietnamese."
    prompt = "What is Python?"
    reply = replying_input(preprompt, prompt)
    print(f"Reply: {reply}")
