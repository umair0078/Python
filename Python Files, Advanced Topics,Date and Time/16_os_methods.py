import os
import shutil
print(os.getcwd())  # gives the current directory on which we are working.
folders = os.listdir("Python Journey")

# os.chdir("/Users")  # changed the directory to users
# print(os.getcwd())
# print(folders)

# for folder in folders:
#     print(folder)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"Python Journey/{folder}"))

# os.remove("demo.txt")  # remove a directory or a file

# To delete Empty Directory Use

os.rmdir("my_directory")

# To delete Empty Directory Use rmtree inside shutil module
# shutil.rmtree("empty")


os .rename("Python Journey/Tutorial 0", "Python Journey/Tutorial") # rename a directory


