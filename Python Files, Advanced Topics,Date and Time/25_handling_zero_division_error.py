number1 = input("Enter the First Number:")
number2 = input("Enter the Second Number:")

try:
    divisionResult = int(number1)/int(number2)
    print(divisionResult)
except ValueError:
    print("Please Enter a valid number!")
except ZeroDivisionError:
    print("Infinity")
