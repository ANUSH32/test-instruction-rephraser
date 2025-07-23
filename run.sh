#!/bin/bash

# Run backend Flask server
echo "Starting backend server on port 5000..."
python3 backend/app.py &

# Run frontend Next.js dev server on port 8000
echo "Starting frontend server on port 8000..."
PORT=8000 npm run dev
