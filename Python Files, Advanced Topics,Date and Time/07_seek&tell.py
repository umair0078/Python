# with open("myFile.txt", "r") as File:
#     readMyFile = File.read(10)  #  only reads first 10 bytes of the file
#     print(readMyFile)

# seek

with open("myFile.txt", "r") as file:
    file.seek(10)  # skip the first 10 characters of the file.
    print(file.tell()) # tell() method returns the current position within the file in bytes.
    readMyFile = file.read(5) # read the next 5 bytes
    current_position = file.tell()
    print(readMyFile)
    print(current_position)
