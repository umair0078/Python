a = 10 # global variable

def my_func():
    a = 20 # local variable of the function
    print(a)


my_func()

def func_2():
    global a
    a = 50   # global a changes to 50
    print(a)

func_2()
    
print(a)
