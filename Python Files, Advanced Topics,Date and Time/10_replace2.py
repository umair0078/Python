fruits = ["Mango", "Orange", "Banana", "Apple"]

with open("fruitsfile.txt", "r") as file:
    readFruit = file.read()

for fruit in fruits:
    readFruit = readFruit.replace(fruit.upper(), "$####$^")
    with open("fruitsfile.txt", "w") as file:
        file.write(readFruit)


print(readFruit)