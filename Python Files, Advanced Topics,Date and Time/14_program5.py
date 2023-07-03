# Files are identical or not ?
file1 = "document.txt"
file2 = "Copy_of_Document.txt"
with open(file1, "r") as file1:
    readFile1 = file1.read()

with open(file2, "r") as file2:
    readFile2 = file2.read()

if readFile1 == readFile2:
    print("Files are Identical")
else:
    print("Files are not Identical!")