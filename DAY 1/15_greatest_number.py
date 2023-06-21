# Program to find greatest number

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number: "))
num4 = int(input("Enter 4th Number: "))

if num1 > num2:
    f1 = num1
else:
    f1 = num2

if num3 > num4:
    f2 = num3
else:
    f2 = num4

if (f1 > f2):
    print(f"The greatest number is:{f1}")
else:
    print(f"The greatest number is:{f2}")
