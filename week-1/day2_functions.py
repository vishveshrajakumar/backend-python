# Day 2: Functions and backend-style logic

def validate_age(age_input):
    if age_input.isdigit():
        age = int(age_input)
        if age > 0:
            return age
        else:
            return None
    else:
        return None


def format_user_data(name, age):
    return f"User Name: {name}, Age: {age}"


# Simulating a backend request
name = input("Enter your name: ")
age_input = input("Enter your age: ")

age = validate_age(age_input)

if age:
    response = format_user_data(name, age)
    print(response)
else:
    print("Invalid age provided.")
