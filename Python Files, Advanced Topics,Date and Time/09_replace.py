with open("myFile.txt") as file:
    readMyFile = file.read()


readMyFile = readMyFile.replace("Adding", "Updating")

with open("myFile.txt", "w") as file:
    file.write(readMyFile)