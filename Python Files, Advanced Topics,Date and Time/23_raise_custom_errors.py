age = int(input("Enter the Age between 18 and 45:"))

if age < 18 or age > 45:
    raise ValueError("Age Should be between 18 and 45")

print(f"Your Entered age is: {age}")

