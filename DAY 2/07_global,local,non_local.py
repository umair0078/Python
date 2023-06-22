greet = "Good Morning!"  # global variable

def func():
    greet2 = "Good Night!"  # local variable of function func()
    print(greet2)


func()

print(greet)



# Non-local Variable

''''nonlocal variables are used in nested functions whose local scope is not defined.
This means that the variable can be neither in the local nor the global scope.'''

def outer_func():
    msg = 'local variable'
    def inner_func():
        nonlocal msg
        msg = "nonlocal variable"  # If we change the value of a nonlocal variable, the changes appear in the local variable.
        print(msg)

    def inner_2():
        print(msg)
       
    inner_func()
    inner_2()

outer_func()



# global keyword

def new_func():
    global greet
    greet = "Good Afternoon!"
    print(greet)


new_func()
print(greet)


def outer_func2():
    num = 2
    def inner():
        global num  # if already global variable exist it changes otherwise it makes new global variable
        num = 4
    print("Before calling inner:", num)
    inner()
    print("After calling inner", num)


outer_func2()
print(num)


