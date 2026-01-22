@echo off
REM Azure AI-900 Study App - Quick Start Script for Windows
REM Run this from inside the "AI-900 Practice" project directory

if not exist venv\ (
    echo ERROR: Virtual environment not found!
    echo.
    echo Make sure you:
    echo 1. Are in the "AI-900 Practice" directory
    echo 2. Have run setup.bat first
    echo.
    echo Current directory: %CD%
    pause
    exit /b 1
)

echo Starting Azure AI-900 Study App...
echo.
call venv\Scripts\activate.bat
python run.py

