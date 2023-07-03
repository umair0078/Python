with open('sample.txt', "w") as file:
    file.write("Hello World!")
    file.truncate(5)  # write only 5 characters in the file

with open("sample.txt", "r") as readFile:
    readMyFile = readFile.read()
    print(readMyFile)
