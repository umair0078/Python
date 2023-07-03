import datetime


def log(func):
    def modified_function(*args, **kwargs):
        with open("logs.txt", "a") as logFile:
            logFile.write("Called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
            func(*args, **kwargs)
    return modified_function

@log
def add(num1, num2, num3=10):
    print(num1+num2+num3)


add(3, 6, 14)
