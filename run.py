#!/usr/bin/env python3
"""
Azure AI-900 Study App Runner

This script starts the Flask development server for the Azure AI-900 study application.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app, init_study_data
    
    if __name__ == '__main__':
        print("🚀 Starting Azure AI-900 Study App...")
        print("📚 Loading study materials...")
        
        # Initialize study data
        init_study_data()
        
        print("✅ Study materials loaded successfully!")
        print("🌐 Starting web server...")
        print("📖 Open your browser to: http://localhost:5000")
        print("⭐ Happy studying! You've got this! 💪")
        print("\n" + "="*50)
        
        # Start the Flask development server
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            use_reloader=True
        )
        
except ImportError as e:
    print("❌ Error: Missing dependencies!")
    print("📦 Please install required packages:")
    print("   pip install -r requirements.txt")
    print(f"\nError details: {e}")
    sys.exit(1)
    
except Exception as e:
    print(f"❌ Error starting the application: {e}")
    print("📧 Please check your study files are in the 'study-files' directory")
    sys.exit(1) 