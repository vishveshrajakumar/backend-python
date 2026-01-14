# Day 4: File handling and JSON persistence

import json
import os

FILE_NAME = "week-1/students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(student_id, name, department):
    students = load_students()

    student = {
        "id": student_id,
        "name": name,
        "department": department
    }

    students.append(student)
    save_students(students)


def list_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)


# Simulating backend requests
add_student(101, "Machii", "CSE")
add_student(102, "Arun", "ECE")

list_students()
