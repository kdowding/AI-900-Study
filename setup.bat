@echo off
REM Azure AI-900 Study App - Windows Setup Script
REM Run this script from inside the "AI-900 Practice" project directory

echo ========================================
echo Azure AI-900 Study App Setup
echo ========================================
echo.
echo Current directory: %CD%
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/4] Python found:
python --version
echo.

REM Check if virtual environment already exists
if exist venv\ (
    echo [2/4] Virtual environment already exists, skipping creation
) else (
    echo [2/4] Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
)
echo.

REM Activate virtual environment and install dependencies
echo [3/4] Installing dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully!
echo.

REM Verify we're in the correct directory
echo [4/4] Verifying project structure...
if not exist "app.py" (
    echo ERROR: app.py not found! Are you in the correct directory?
    echo This script must be run from inside the "AI-900 Practice" folder
    echo Current directory: %CD%
    pause
    exit /b 1
)

if not exist "study-files\Azure AI-900 Practice Quiz.md" (
    echo WARNING: Study files may be missing in the study-files directory
    echo Please ensure all required .md files are present
)
echo Verification complete!
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the app:
echo   1. Run: venv\Scripts\activate
echo   2. Run: python run.py
echo   3. Open: http://localhost:5000
echo.
echo Or simply run: start.bat
echo.
pause

