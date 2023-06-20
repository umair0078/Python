# Grade Calculation
marks = int(input("Enter Your Marks:"))
if marks > 60:
    grade = "Invalid"
elif marks >= 48 and marks <= 60:
    grade = "A"
elif marks >= 39 and marks <= 47:
    grade = "B"
elif marks >= 30 and marks <= 39:
    grade = "C"
elif marks >= 24 and marks <=30:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")