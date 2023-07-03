# reading a file
# file = open("introduction.txt", "r")  # rt also opens file in the text mood but rb opens the file in the binary mood.

# readFile = file.read()
# print(readFile)
# file.close()

# writing to a file

# file = open("myFile.txt", "w")

# file.write("Hello, This is my new file!")

# file.close()

# appending to a file

file = open("myFile.txt", "a")

file.write("Adding New Content...")

file.close()

# If you don't want to close the file you can use "with" before "open()"

with open("myFile.txt","a") as myFile:
    myFile.write("\n2023")

with open("myFile.txt", "r") as newFile:
    readMyFile = newFile.read()
    print(readMyFile)