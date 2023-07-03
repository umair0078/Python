try:
    num = int(input("Enter a number:"))

    print(f"The Multiplication table of the number is : {num}")

    for number in range(1,11):
        print(f"{num}*{number}={num*number}")
# except Exception as e:
#     print(e)
except:
    print("Invalid Input!")
print("Lines to be executed.")
print("End")