# openFile = open("newFile.txt", "w")

# fruits = ["Mango", "Orange", "Banana"]

# openFile.writelines(fruits)

openFile = open("newFile.txt", "a")

fruits = ["Srawberry", "Grapes", "Palm"]

for fruit in fruits:
    openFile.writelines(fruit + "\n")
 