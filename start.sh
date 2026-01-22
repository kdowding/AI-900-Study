#!/bin/bash
# Azure AI-900 Study App - Quick Start Script for macOS/Linux
# Run this from inside the "AI-900 Practice" project directory

if [ ! -d "venv" ]; then
    echo "ERROR: Virtual environment not found!"
    echo ""
    echo "Make sure you:"
    echo "1. Are in the 'AI-900 Practice' directory"
    echo "2. Have run ./setup.sh first"
    echo ""
    echo "Current directory: $(pwd)"
    exit 1
fi

echo "Starting Azure AI-900 Study App..."
echo ""
source venv/bin/activate
python run.py

