# The code inside finally will always executed either it will go to try or except
try:
    list_of_numbers = [2,34,56,23,83,12]
    index = int(input("Enter the index number: "))
    print(list_of_numbers[index])
except:
    print("Exception Occurred!")
    exit()
finally:
    print("It will always execute!")


print("It will always execute")