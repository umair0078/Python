def greet(func):
    def modified_function(*args, **kwargs):
        print("Good Morning")
        val = func(*args, **kwargs)
        print("Thanks for using this function")
        return val
        
    return modified_function

# @greet
def hello():
    print("Hello Everyone!")

# hello()

# greet(hello)()
greeting = greet(hello)
greeting()
# @greet
def add(num1,num2):
    return num1+num2

# add(2,3)

# greet(add)(2,4)

adding = greet(add)
print(adding(3,6))
