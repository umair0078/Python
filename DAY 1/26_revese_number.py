# Program to reverse a number Entered by the user

n = int(input("Enter a number: "))

while n > 0:
    r = n % 10  # remainder will be the last digit of the number entered by the user
    print(r, end="")
    n = n // 10  


