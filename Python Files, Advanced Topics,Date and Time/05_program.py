with open("sample.txt") as file:
    readMyFile = file.read()

if "Hello".lower or "Hello".upper() in readMyFile:
    print("Hello is present")
else:
    print("Hello is not present")