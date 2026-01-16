# Day 5: Error handling and validation

import json
import os

FILE_NAME = "week-1/students.json"


def load_students():
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Error: Data file is corrupted.")
        return []

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def validate_student(student_id, name, department):
    if not isinstance(student_id, int):
        return False

    if not name or not department:
        return False

    return True


def add_student(student_id, name, department):
    if not validate_student(student_id, name, department):
        print("Invalid student data provided.")
        return

    students = load_students()

    student = {
        "id": student_id,
        "name": name,
        "department": department
    }

    students.append(student)

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

    except Exception as e:
        print(f"Failed to save data: {e}")


def list_students():
    students = load_students()

    if not students:
        print("No students available.")
        return

    for student in students:
        print(student)


# Simulated backend calls
add_student(103, "Kumar", "IT")
add_student("abc", "", "")
list_students()
