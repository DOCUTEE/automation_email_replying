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
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"HTTP error: {e}")
    except (ValueError, KeyError) as e:
        print(f"Response parse error: {e}")
    return None

if __name__ == "__main__":
    preprompt = "Only reply in Vietnamese."
    prompt = "What is Python?"
    reply = replying_input(preprompt, prompt)
    print(f"Reply: {reply}")
