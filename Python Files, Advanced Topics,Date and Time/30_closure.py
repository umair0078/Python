# closure: creating nested function
def outer_func():
    x = 100
    def inner_func():
        y = 50
        return x+y
    return inner_func()

outer = outer_func()

print(outer)

# Another Example

def greet(name):
    def say_hello():
        print("Hello " + name)
    say_hello()

greet("Umair")