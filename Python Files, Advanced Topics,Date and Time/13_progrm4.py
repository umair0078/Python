# copy the content of on file to another file

with open("document.txt", "r") as document:
    documentContent = document.read()

with open("Copy_of_Document.txt", "w") as document:
    document.write(documentContent)