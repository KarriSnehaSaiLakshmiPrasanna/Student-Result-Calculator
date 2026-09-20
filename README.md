# Student Result Calculator

A complete Student Result Calculator built with Python Flask, HTML, CSS, JavaScript and SQLite.

## Features
- Add student results
- Five subjects: English, Mathematics, Science, Social Studies, Computer
- Automatic total, percentage, grade and pass/fail
- Search by name or student ID
- Edit and delete student records
- Printable result card
- SQLite database
- JSON API at `/api/students`

## Run on Windows
1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Create a virtual environment:
   `python -m venv venv`
4. Activate it:
   `venv\Scripts\activate`
5. Install packages:
   `pip install -r requirements.txt`
6. Start:
   `python app.py`
7. Open `http://127.0.0.1:5000`

## Run on macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

The SQLite database `students.db` is created automatically on first run.
