# myFile = open("myFile.txt", "r")
# readLine = myFile.readline()  # read line-by-line
# print(readLine)

# myFile = open("myFile.txt","r")

# while True:
#     line = myFile.readline()
#     print(line)
#     if not line:
#         break

myFile = open("marks.txt", "r")
i = 0
while True:
    i += 1
    readLine = myFile.readline()
    print(readLine)
    
    if not readLine:
        break
    m1 = int(readLine.split(",")[0])
    m2 = int(readLine.split(",")[1])
    m3 = int(readLine.split(",")[2])
    print(f"The marks of student {i} in Math : {m1*2}")
    print(f"The marks of student {i} in English : {m2*2}")
    print(f"The marks of student {i} in Physics : {m3*2}")


# Practice
# myFile = open("marks.txt", "r")

# line = myFile.readline()
# print(line)