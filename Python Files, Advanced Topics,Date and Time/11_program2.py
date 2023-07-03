with open("document.txt", "r") as file:
    readDocument = file.read()

if 'python'.lower() in readDocument:
    print("Yes, Python is present")
else:
    print("No, Python is not present")