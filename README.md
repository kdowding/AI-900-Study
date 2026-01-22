# Azure AI-900 Study App 📚

A comprehensive web-based study application designed to help you master the Microsoft Azure AI-900 certification exam through interactive learning, bite-sized content delivery, and practice quizzes.

## ✨ What's Included

- **5 Complete Study Topics** covering all AI-900 exam areas
- **50-Question Practice Quiz** with detailed explanations
- **Flashcard System** for quick memorization
- **Progress Tracking** to monitor your advancement
- **Quick Review Mode** for last-minute preparation
- **Interactive Dashboard** with study statistics

### Study Content Coverage

1. **Artificial Intelligence Workloads and Considerations (15-20%)**
2. **Fundamental Principles of Machine Learning on Azure (15-20%)**
3. **Computer Vision Workloads on Azure (15-20%)**
4. **Natural Language Processing Workloads on Azure (15-20%)**
5. **Generative AI Workloads on Azure (20-25%)**

---

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended) ⭐

**Windows:**
```bash
# 1. Run automated setup (creates venv, installs dependencies)
setup.bat

# 2. Start the app
start.bat

# 3. Open http://localhost:5000 in your browser
```

**macOS/Linux:**
```bash
# 1. Make scripts executable and run setup
chmod +x setup.sh start.sh
./setup.sh

# 2. Start the app
./start.sh

# 3. Open http://localhost:5000 in your browser
```

### Option 2: Manual Setup

If you prefer to set up step-by-step or the automated scripts don't work, follow the detailed instructions below.

---

## 📋 Detailed Setup Instructions

### Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** ([Download here](https://python.org/downloads/))
  - ⚠️ **Windows users**: Check "Add Python to PATH" during installation
- **Git** (optional, for cloning) or download as ZIP
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

### Step 1: Get the Code

**Download ZIP**
- Download the ZIP file
- Extract to a folder on your computer

### Step 2: Navigate to Project Directory

**This is important!** You must be inside the project directory before proceeding.

```bash
# Navigate into the project folder
cd "AI-900 Practice"

# Verify you're in the right place (should show app.py, run.py, etc.)
# Windows:
dir

# macOS/Linux:
ls
```

You should see files like `app.py`, `run.py`, `requirements.txt`, and folders like `study-files/` and `templates/`.

### Step 3: Create Virtual Environment

**Why?** A virtual environment isolates this app's dependencies from other Python projects on your system.

**⚠️ Make sure you're in the project directory first!**

**Windows:**
```bash
# Create virtual environment (run this from the AI-900 Practice directory)
python -m venv venv

# Activate it
venv\Scripts\activate

# You should now see (venv) at the start of your command prompt
```

**macOS/Linux:**
```bash
# Create virtual environment (run this from the AI-900 Practice directory)
python3 -m venv venv

# Activate it
source venv/bin/activate

# You should now see (venv) at the start of your terminal prompt
```

### Step 4: Install Dependencies

**Make sure your virtual environment is activated** (you should see `(venv)` in your prompt).

```bash
# Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed Flask-2.3.3 Werkzeug-2.3.7 Jinja2-3.1.2 MarkupSafe-2.1.3 
itsdangerous-2.1.2 click-8.1.7 blinker-1.6.3 Markdown-3.5.1 python-dotenv-1.0.0
```

### Step 5: Run the Application

**Windows:**
```bash
python run.py
```

**macOS/Linux:**
```bash
python run.py
```

**Expected output:**
```
🚀 Starting Azure AI-900 Study App...
📚 Loading study materials...
✅ Study materials loaded successfully!
🌐 Starting web server...
📖 Open your browser to: http://localhost:5000
⭐ Happy studying! You've got this! 💪
==================================================
```

### Step 6: Open in Browser

Navigate to: **http://localhost:5000**

🎉 **You're ready to start studying!**

---

## 🔄 Daily Usage

After the initial setup, here's how to use the app each time:

### Using the Quick Start Scripts

**Windows:**
```bash
cd "AI-900 Practice"
start.bat
```

**macOS/Linux:**
```bash
cd "AI-900 Practice"
./start.sh
```

### Manual Start

```bash
# 1. Navigate to project directory
cd "AI-900 Practice"

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# 3. Run the app
python run.py

# 4. Open http://localhost:5000 in browser
```

### When You're Done

Press `Ctrl+C` in the terminal to stop the app, then:

```bash
# Deactivate virtual environment
deactivate
```

---

## 🛠️ Troubleshooting

### "Python is not recognized" (Windows)

**Problem:** Python isn't installed or not in PATH

**Solution:**
1. Reinstall Python from [python.org](https://python.org/downloads/)
2. ✅ Check "Add Python to PATH" during installation
3. Restart your terminal/command prompt
4. Try `py` instead of `python` if still having issues

### "No module named 'flask'" or Similar Import Errors

**Problem:** Dependencies not installed or virtual environment not activated

**Solution:**
1. Make sure you see `(venv)` in your command prompt
2. If not, activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

### "Cannot find path venv\Scripts\activate"

**Problem:** Virtual environment doesn't exist or you're in the wrong directory

**Solution:**
1. Make sure you're in the project directory: `cd "AI-900 Practice"`
2. Create the virtual environment: `python -m venv venv`
3. Then activate it

### "Port 5000 is already in use"

**Problem:** Another application is using port 5000

**Solution:**
- Close other applications that might be using port 5000
- OR edit `run.py` line 34 to use a different port (e.g., `port=5001`)

### "Study materials not found"

**Problem:** Study files are missing

**Solution:**
1. Verify you cloned the complete repository
2. Check that `study-files/` directory exists and contains 8 `.md` files
3. Re-clone the repository if files are missing

### Application Starts But Browser Can't Connect

**Problem:** Firewall or network issue

**Solution:**
- Verify the app is running (look for "Running on http://localhost:5000")
- Try `http://127.0.0.1:5000` instead
- Check firewall settings
- Try a different browser

---

## 📖 How to Use the Study App

### Dashboard
- View your overall progress and study statistics
- Navigate to any of the 5 study topics
- Continue where you left off
- Access quizzes and review mode

### Study Mode
- Content is broken into bite-sized, digestible chunks
- Navigate using Previous/Next buttons
- Track your progress through each topic
- Mark topics as complete

### Practice Quizzes
- Take full practice exams with 50 questions
- Get immediate feedback on your answers
- Review detailed explanations
- Retake as many times as needed to reach 80%+

### Flashcards
- Study key terms and concepts
- Track mastered cards
- Review difficult cards
- Build muscle memory for exam terms

### Review Mode
- Quick reference guide for key concepts
- Searchable content to find specific topics
- Last-minute exam prep strategies
- Azure services overview

---

## 🎯 Study Strategy

### Recommended 4-Week Plan

**Week 1-2:** Complete Topics 1-3 (AI Fundamentals & ML)
**Week 3:** Complete Topics 4-5 (Computer Vision, NLP, Generative AI)
**Week 4:** Review mode + practice quizzes (aim for 80%+ consistently)

### Study Tips

- ✅ Study in **short daily bursts** (15-20 min) rather than long sessions
- ✅ **Focus on Azure-specific** services and their capabilities
- ✅ Take **quizzes after each topic** to reinforce learning
- ✅ Use **flashcards** for memorizing service names and key terms
- ✅ **Review weak areas** identified by quiz results

### Exam Success Metrics

- [ ] Complete all 5 study topics
- [ ] Score 80%+ on practice quizzes consistently
- [ ] Review all flashcards and master key terms
- [ ] Understand Responsible AI principles thoroughly

---

## 🛠️ Technical Details

### Built With

- **Flask** - Python web framework
- **Bootstrap 5** - Responsive UI
- **Markdown** - Content formatting
- **JavaScript** - Interactive features and progress tracking

### Project Structure

```
AI-900 Practice/
├── app.py                  # Main Flask application
├── run.py                  # Application startup script
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── setup.bat              # Windows setup script
├── setup.sh               # macOS/Linux setup script
├── start.bat              # Windows start script
├── start.sh               # macOS/Linux start script
├── venv/                  # Virtual environment (created during setup)
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── study.html
│   ├── quiz.html
│   ├── review.html
│   └── flashcards.html
└── study-files/           # Study materials (8 markdown files)
    ├── Azure AI-900 Exam Study Guide Outline.md
    ├── Azure AI-900 Exam Study Guide_ Topic 1.md
    ├── Azure AI-900 Exam Study Guide_ Topic 2.md
    ├── Azure AI-900 Exam Study Guide_ Topic 3.md
    ├── Azure AI-900 Exam Study Guide_ Topic 4.md
    ├── Azure AI-900 Exam Study Guide_ Topic 5.md
    ├── Azure AI-900 Exam Study Guide_ Key Essentials.md
    └── Azure AI-900 Practice Quiz.md
```

**Note:** The `venv/` directory is automatically excluded from git (via `.gitignore`) and should never be committed.

### System Requirements

- **Python:** 3.8 or higher
- **RAM:** 512MB minimum (1GB recommended)
- **Disk Space:** ~50MB
- **OS:** Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)

---

## ❓ FAQ

**Q: Do I need to activate the virtual environment every time?**  
A: Yes, each time you open a new terminal session. You'll see `(venv)` when it's activated. The quick start scripts (`start.bat`/`start.sh`) do this automatically.

**Q: Can I delete the venv folder?**  
A: Yes! If something goes wrong, delete the `venv/` folder and run `setup.bat` or `setup.sh` again to start fresh.

**Q: Does my progress save?**  
A: Progress is saved in your browser's session storage. It persists while you study but resets when you close the browser.

**Q: Can I run this on multiple computers?**  
A: Yes! Just clone the repository and set up the virtual environment on each computer.

**Q: Is this the official Microsoft study material?**  
A: No, this is a third-party study tool created to help you prepare for the AI-900 exam.

---

## 🎓 Ready to Get Started?

1. Choose either **automated** or **manual** setup above
2. Follow the steps for your operating system
3. Start studying!
4. Good luck on your AI-900 exam! 💪

**Questions?** Review the Troubleshooting section or check that all prerequisites are met.

---