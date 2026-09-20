from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "student-result-calculator-secret"
DB = Path(__file__).with_name("students.db")

SUBJECTS = ["English", "Mathematics", "Science", "Social Studies", "Computer"]

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                class_name TEXT NOT NULL,
                english REAL NOT NULL,
                mathematics REAL NOT NULL,
                science REAL NOT NULL,
                social_studies REAL NOT NULL,
                computer REAL NOT NULL,
                total REAL NOT NULL,
                percentage REAL NOT NULL,
                grade TEXT NOT NULL,
                result TEXT NOT NULL
            )
        """)

def calculate(marks):
    total = sum(marks)
    percentage = total / len(marks)
    if any(m < 35 for m in marks):
        result = "Fail"
    else:
        result = "Pass"

    if result == "Fail":
        grade = "F"
    elif percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "F"
    return total, percentage, grade, result

@app.route("/")
def index():
    search = request.args.get("search", "").strip()
    with get_db() as conn:
        if search:
            students = conn.execute(
                "SELECT * FROM students WHERE name LIKE ? OR student_id LIKE ? ORDER BY id DESC",
                (f"%{search}%", f"%{search}%")
            ).fetchall()
        else:
            students = conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    return render_template("index.html", students=students, search=search)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        try:
            student_id = request.form["student_id"].strip()
            name = request.form["name"].strip()
            class_name = request.form["class_name"].strip()
            marks = [float(request.form[s]) for s in
                     ["english","mathematics","science","social_studies","computer"]]

            if not student_id or not name or not class_name:
                raise ValueError("Please fill in all student details.")
            if any(m < 0 or m > 100 for m in marks):
                raise ValueError("Marks must be between 0 and 100.")

            total, percentage, grade, result = calculate(marks)
            with get_db() as conn:
                conn.execute("""
                    INSERT INTO students
                    (student_id,name,class_name,english,mathematics,science,
                     social_studies,computer,total,percentage,grade,result)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                """, (student_id,name,class_name,*marks,total,percentage,grade,result))
            flash("Student result added successfully.", "success")
            return redirect(url_for("index"))
        except sqlite3.IntegrityError:
            flash("Student ID already exists.", "error")
        except (ValueError, KeyError):
            flash("Please enter valid details and marks from 0 to 100.", "error")
    return render_template("form.html", student=None, subjects=SUBJECTS)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    with get_db() as conn:
        student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    if not student:
        return "Student not found", 404

    if request.method == "POST":
        try:
            student_id = request.form["student_id"].strip()
            name = request.form["name"].strip()
            class_name = request.form["class_name"].strip()
            marks = [float(request.form[s]) for s in
                     ["english","mathematics","science","social_studies","computer"]]
            if not student_id or not name or not class_name:
                raise ValueError
            if any(m < 0 or m > 100 for m in marks):
                raise ValueError

            total, percentage, grade, result = calculate(marks)
            with get_db() as conn:
                conn.execute("""
                    UPDATE students SET student_id=?, name=?, class_name=?,
                    english=?, mathematics=?, science=?, social_studies=?,
                    computer=?, total=?, percentage=?, grade=?, result=?
                    WHERE id=?
                """, (student_id,name,class_name,*marks,total,percentage,grade,result,id))
            flash("Student result updated successfully.", "success")
            return redirect(url_for("index"))
        except sqlite3.IntegrityError:
            flash("Student ID already exists.", "error")
        except (ValueError, KeyError):
            flash("Please enter valid details and marks from 0 to 100.", "error")

    return render_template("form.html", student=student, subjects=SUBJECTS)

@app.post("/delete/<int:id>")
def delete_student(id):
    with get_db() as conn:
        conn.execute("DELETE FROM students WHERE id=?", (id,))
    flash("Student deleted.", "success")
    return redirect(url_for("index"))

@app.route("/result/<int:id>")
def result_card(id):
    with get_db() as conn:
        student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    if not student:
        return "Student not found", 404
    return render_template("result.html", student=student, subjects=SUBJECTS)

@app.get("/api/students")
def api_students():
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    return jsonify([dict(r) for r in rows])

init_db()

if __name__ == "__main__":
    app.run(debug=True)