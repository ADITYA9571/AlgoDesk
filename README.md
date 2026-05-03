<img width="1919" height="1006" alt="Screenshot 2026-04-30 221058" src="https://github.com/user-attachments/assets/70f29148-5934-417b-9c80-4eafca97f2b9" />

# AlgoDesk

AlgoDesk is a desktop DSA revision app built with Python, HTML, CSS, and JavaScript. It provides a dark-themed dashboard for browsing algorithm topics, tracking progress, searching concepts, and reviewing code snippets in a clean desktop interface.

## Features

- Dark-only product-style dashboard UI
- Topic progress tracking with automatic save
- Section-wise navigation and filtering
- Search across sections and topics
- Collapsible study cards
- Copy-ready code blocks
- Desktop packaging with PyInstaller

## Tech Stack

- Python
- pywebview
- HTML
- CSS
- JavaScript
- PyInstaller

## Project Files

- `app.py` - desktop app entry point
- `dsa_notes_interview_cp.html` - main UI structure and app logic
- `dsa_notes_interview_cp.css` - app styling
- `AlgoDesk.spec` - PyInstaller build configuration
- `icon1.ico` - application icon

## Progress Storage

User progress is saved automatically to a local JSON file on the machine running the app.

Typical Windows path:

```text
%APPDATA%\AlgoDesk\state.json
```

This file is runtime data and is not part of the source repository.

## Installation

1. Create and activate a virtual environment.
2. Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Run the App

```powershell
python app.py
```

## Build the EXE

Using the included PyInstaller spec file:

```powershell
pyinstaller --clean AlgoDesk.spec
```

The built executable will be created in:

```text
dist\AlgoDesk.exe
```

## Files to Share for Rebuild

If someone wants to rebuild the app, these are the important files:

- `app.py`
- `dsa_notes_interview_cp.html`
- `dsa_notes_interview_cp.css`
- `AlgoDesk.spec`
- `icon1.ico`
- `requirements.txt`

## Do Not Commit

These should stay out of Git:

- `build/`
- `dist/`
- `__pycache__/`
- local app progress JSON from `%APPDATA%\AlgoDesk\state.json`

## Notes

- The app UI is dynamic and rendered from local JavaScript data.
- Progress is saved through Python into a JSON file, not a database.
- The packaged desktop app is built using PyInstaller.
