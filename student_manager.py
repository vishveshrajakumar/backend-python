# Week 1 Consolidation: Student Manager Backend

import json
import os

FILE_NAME = "week-1/students.json"


def load_students():
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except Exception:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def validate_student(student_id, name, department):
    return isinstance(student_id, int) and name and department


def add_student(student_id, name, department):
    if not validate_student(student_id, name, department):
        print("Invalid student data.")
        return

    students = load_students()
    students.append({
        "id": student_id,
        "name": name,
        "department": department
    })

    save_students(students)
    print("Student added successfully.")


def list_students():
    students = load_students()
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)


# Simulated backend operations
add_student(201, "Machii", "CSE")
add_student(202, "Arun", "ECE")
list_students()
