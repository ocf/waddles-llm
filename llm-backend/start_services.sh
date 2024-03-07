#!/bin/bash

# Start ollama serve in the background
ollama serve > /dev/null 2>&1 &

# Verbosity stating server is initializing
echo "[BACKEND] Ollama backend initializing ..."

# Wait for ollama serve to start (you might need to adjust the sleep duration)
sleep 7

# Print that Ollama has initialized
echo "[BACKEND] Ollama backend initialized!"

# Verbosity stating the model is being pulled
echo "[BACKEND] Pulling main model ..."

# Pull the Mixtral8x7b model file
ollama pull qwen:1.8b && echo "[BACKEND] Main Model pulled!" || echo "[BACKEND] Main Model pull failed!"

# Verbosity that retriever model is being pulled
echo "[BACKEND] Pulling retriever model ..."

# Pull the qwen:1.8b model file
ollama pull qwen:1.8b && echo "[BACKEND] Retriever Model pulled!" || echo "[BACKEND] Retriever Model pull failed!"

# Create the database directory if it doesn't exist
echo "[BACKEND] Creating database directory"
mkdir -p knowledge_db/database

# Run the poetry command to start the backend
echo "[BACKEND] Starting server ..."
poetry run python3.9 waddles.py

# Keep the script running (the trap command ensures proper cleanup on container exit)
exit_code=$?

# Exit the script with the exit code of the main process
# exit $exit_code

trap "exit 0" INT TERM
# tail -f /dev/null
