# Student Complaint Register

A simple Flask web application for registering and viewing student complaints.

## Features

- Add student complaints
- Select complaint category
- View submitted complaints
- JSON API for complaints
- Health check endpoint
- Server-side input validation
- Automated tests using pytest
- Code linting using flake8

## Technology

- Python
- Flask
- HTML
- pytest
- flake8
- Git
- GitHub Actions
- Docker
- Render

## API Endpoints

- `/` - Home page
- `/add` - Add a complaint
- `/api/complaints` - Complaint JSON API
- `/health` - Application health check

(venv) PS C:\Users\HP\ty cse\student-complaint-register> git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

## How to Run Locally

1. Create a virtual environment:

   python -m venv venv

2. Activate the virtual environment:

   venv\Scripts\activate

3. Install dependencies:

   pip install -r requirements.txt

4. Start the application:

   python app.py

5. Open the application in a browser:

   http://127.0.0.1:5000