#!/bin/bash
# Azure AI-900 Study App - macOS/Linux Setup Script
# Run this script from inside the "AI-900 Practice" project directory

echo "========================================"
echo "Azure AI-900 Study App Setup"
echo "========================================"
echo ""
echo "Current directory: $(pwd)"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://python.org/downloads/"
    echo "Or use your package manager (brew, apt, dnf, etc.)"
    exit 1
fi

echo "[1/4] Python found:"
python3 --version
echo ""

# Check if virtual environment already exists
if [ -d "venv" ]; then
    echo "[2/4] Virtual environment already exists, skipping creation"
else
    echo "[2/4] Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
    echo "Virtual environment created successfully!"
fi
echo ""

# Activate virtual environment and install dependencies
echo "[3/4] Installing dependencies..."
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "Dependencies installed successfully!"
echo ""

# Verify we're in the correct directory
echo "[4/4] Verifying project structure..."
if [ ! -f "app.py" ]; then
    echo "ERROR: app.py not found! Are you in the correct directory?"
    echo "This script must be run from inside the 'AI-900 Practice' folder"
    echo "Current directory: $(pwd)"
    exit 1
fi

if [ ! -f "study-files/Azure AI-900 Practice Quiz.md" ]; then
    echo "WARNING: Study files may be missing in the study-files directory"
    echo "Please ensure all required .md files are present"
fi
echo "Verification complete!"
echo ""

echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To start the app:"
echo "  1. Run: source venv/bin/activate"
echo "  2. Run: python run.py"
echo "  3. Open: http://localhost:5000"
echo ""
echo "Or simply run: ./start.sh"
echo ""

