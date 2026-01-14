# Day 3: Lists and dictionaries (backend data handling)

students = []

def add_student(student_id, name, department):
    student = {
        "id": student_id,
        "name": name,
        "department": department
    }
    students.append(student)

def list_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)


# Simulating backend requests
add_student(101, "Machii", "CSE")
add_student(102, "Arun", "ECE")

list_students()
