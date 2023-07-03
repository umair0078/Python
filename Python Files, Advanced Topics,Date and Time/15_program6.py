# Program to empty a specific file
filename = "myFile.txt"

with open(filename, "w") as openMyFile:
    openMyFile.write("")