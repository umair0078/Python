list_of_numbers = [23, 4, 56, 32, 45, 62, 45, 94]
index = input("Please Enter the index number:")
try:
    print(list_of_numbers[int(index)])
except ValueError:
    print("Invalid Input!")
except IndexError:
    print("Invalid Index Number!")


