name=input()
age=input()
if age.isdigit():
    age=int(age)
    if age>0:
        print(f"Hi {name} your age is {age}")
    elif age<0:
        print("age cant be 0")
else:
    print("Enter age values in digits")