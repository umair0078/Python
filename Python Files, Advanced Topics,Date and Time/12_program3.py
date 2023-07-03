# In which line number the Python is present in document.txt
content = True
line = 1

with open("document.txt", "r") as file:
    while content:
        content = file.readline()
        if 'python' in content.lower():
            print(f"Yes Python is present in line: {line}")
        line += 1



