def cube(num):
    print(num**3)

print(__name__)  # output: __main__ means it is running from the same file in which it is written.
if __name__ == "__main__":
    cube(2)

