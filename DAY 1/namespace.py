'''
A namespace containing all the built-in names is created when we start the Python interpreter and exists as long as the interpreter runs.

This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program.
Each module creates its own global namespace.Modules can have various functions and classes.
A local namespace is created when a function is called, which has all the names defined in it.
'''

global_var = 10   # global_var is in the global namespace

def outer_func():
    outer_local_var = 20    # outer_local_var is in the local namespace

    def inner_func():
        inner_local_var = 30  # inner_local_var is in the nested local namespace
        print(inner_local_var)
    
    print(outer_local_var)

    inner_func()
    


outer_func()
