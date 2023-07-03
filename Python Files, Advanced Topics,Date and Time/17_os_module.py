import os
print(os.listdir())
if not os.path.exists("Python Journey"):
    os.mkdir("Python Journey")

for folder in range(100):
    os.mkdir(f"Python Journey/Day{folder}")