# Finally will always execute even function is returned.
list_of_numbers = [23,45,67,89,23,45,1]

def findVlaue():
    try:
        index = input("Enter Index Number:")
        print(list_of_numbers[int(index)])
        return 1
    except:
        print("Exception Occurred!")
        return 0
    finally:
        print("It will always execute!")

print(findVlaue())