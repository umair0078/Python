value = input("Enter any number between 10 and 15:")

if value == 'quit':
    print(f"You Entered: {value}")
elif int(value) < 10 or int(value) > 15:
    raise ValueError("Number should be between 10 and 15")

print(value)



