#!/bin/sh
ollama serve &

# Wait for server to start
sleep 5

# Preload model (optional, but avoids long load times later)
ollama pull gemma3:1b

# Keep container alive
tail -f /dev/null
