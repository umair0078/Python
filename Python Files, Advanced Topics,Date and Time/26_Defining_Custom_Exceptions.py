class CustomError(Exception):
    ...
    pass
try:
    ...
except:
    ...

# Defining Custom Exceptions
class InvalidAgeException(Exception):
    "Age less than 18"

try:
    age = int(input("Enter Your Age:"))
    if age< 18:
        raise InvalidAgeException
    else:
        print("You're Eligible to vote!")
except ValueError:
    print("invalid Value!")
except InvalidAgeException:
    print("Exception Occurred: Invalid Age!")


    