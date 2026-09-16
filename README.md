# Screen Assistant

A Python-based AI assistant built with Flask and Gemini, with persistent conversation history using SQLite.

The project is being developed incrementally, with the goal of adding screen-aware capabilities such as analyzing screenshots, explaining visible code, and helping understand on-screen errors.

## Features

* Flask-based web interface
* Gemini API integration
* Conversational AI using Gemini chat sessions
* Persistent conversation history with SQLite
* HTML/CSS frontend
* Environment-variable configuration for API credentials

## Tech Stack

* **Python**
* **Flask**
* **Google Gemini API**
* **SQLite**
* **HTML**
* **CSS**
* **Git & GitHub**

## Project Structure

```text
screen_assistant/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── .env
├── .gitignore
├── app.py
├── database.py
└── requirements.txt
```

> `.env` and `assistant.db` are local files and are excluded from Git.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Azaucifer/screen_assistant.git
cd screen_assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Gemini API key.

**Never commit your API key to Git.**

### 5. Run the application

```powershell
python app.py
```

Open the local Flask address shown in the terminal.

## How It Works

The current application follows this flow:

```text
User
  ↓
Flask Web Interface
  ↓
Gemini API
  ↓
AI Response
  ↓
SQLite
  ↓
Conversation History
  ↓
Browser
```

User questions and assistant responses are stored in SQLite.

The Gemini chat session maintains conversational context while the application is running, while SQLite provides persistent storage for the conversation history.

## Roadmap

* [x] Flask application
* [x] Basic web interface
* [x] Gemini API integration
* [x] Conversational chat
* [x] SQLite conversation history
* [ ] Restore Gemini conversation context from SQLite after application restart
* [ ] Screen capture
* [ ] Vision-based screen analysis
* [ ] Explain code visible on screen
* [ ] Explain errors visible on screen
* [ ] Additional assistant modes
* [ ] Automated tests
* [ ] CI integration
* [ ] Optional desktop interface

## Status

**Early development**

The current version provides the foundation for a Python-based AI screen assistant. Screen-aware and desktop-oriented functionality will be added incrementally.
