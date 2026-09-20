# 🎓 Student Result Calculator

A simple and user-friendly **Student Result Calculator Web Application** built using **Python Flask, HTML, CSS, JavaScript, and SQLite**.

This project allows users to add student details and subject marks, automatically calculate the total marks, percentage, grade, and pass/fail result, and generate a printable result card.

## 🚀 Features

* 👨‍🎓 Add student details
* 📝 Enter subject-wise marks
* 🧮 Automatically calculate total marks
* 📊 Automatically calculate percentage
* 🏆 Automatic grade calculation
* ✅ Pass/Fail result calculation
* 🔍 Search students by name or student ID
* ✏️ Edit student results
* 🗑️ Delete student records
* 📄 Generate and print student result cards
* 💾 Store data using SQLite database
* 📱 Responsive user interface
* 🔗 JSON API for student records

## 📚 Subjects

The application currently includes five subjects:

1. English
2. Mathematics
3. Science
4. Social Studies
5. Computer

Each subject is calculated out of **100 marks**, making the maximum total **500 marks**.

## 📈 Grading System

| Percentage | Grade |
| ---------- | ----- |
| 90% – 100% | A+    |
| 80% – 89%  | A     |
| 70% – 79%  | B+    |
| 60% – 69%  | B     |
| 50% – 59%  | C     |
| 35% – 49%  | D     |
| Below 35%  | F     |

A student receives **Fail** if they score below 35 marks in any subject.

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **JavaScript**
* **SQLite**
* **Jinja2**

## 📂 Project Structure

```text
student_result_calculator/
│
├── app.py
├── requirements.txt
├── README.md
├── students.db
│
├── templates/
│   ├── index.html
│   ├── form.html
│   └── result.html
│
└── static/
    ├── style.css
    └── script.js
```

> `students.db` is created automatically when the application is started for the first time.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/student-result-calculator.git
```

### 2. Open the project folder

```bash
cd student-result-calculator
```

### 3. Create a virtual environment

**Windows:**

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

### 6. Open in your browser

```text
http://127.0.0.1:5000
```

## 🖥️ How It Works

### Step 1 — Add Student

Enter:

* Student ID
* Student Name
* Class
* Marks for each subject

### Step 2 — Automatic Calculation

The application automatically calculates:

```text
Total Marks
Percentage
Grade
Pass/Fail
```

### Step 3 — View Result

The saved student appears in the student results table.

You can:

* 👁️ View the result
* ✏️ Edit the result
* 🗑️ Delete the result

### Step 4 — Print Result Card

Click **View** to open the student's result card.

The result card can be printed using the **Print Result** button.

## 🔗 API

The project also provides a simple API endpoint:

```text
GET /api/students
```

This returns student records in JSON format.

Example:

```json
[
  {
    "student_id": "ST001",
    "name": "John",
    "class_name": "10-A",
    "total": 425,
    "percentage": 85,
    "grade": "A",
    "result": "Pass"
  }
]
```

## 🔮 Future Improvements

Possible features that can be added in future versions:

* 👤 Student login and admin login
* 📊 Result charts and graphs
* 📥 Export results to PDF
* 📑 Export results to Excel
* 🏫 School/college name and logo
* 📧 Email result cards
* 📱 Mobile-friendly improvements
* 🥇 Student ranking system
* 📅 Academic year and semester selection
* 🔐 User authentication
* ☁️ Online database support

## 🎯 Project Objective

The main objective of this project is to create a simple web-based system that reduces manual calculation of student results and provides a convenient way to manage and view academic performance.

## 👨‍💻 Author

KARRI SNEHA SAI LAKSHMI PRASANNA

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
