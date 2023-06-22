# args:
# we can give any number of arguments and python will pack these arguments into a tuple.
# write * before giving argument to the function

def pack_args(*args):
    print(args)
    print(type(args))


x = "Hello"
y = "Good Morrning"
z = 7

pack_args(x,y,z)

# Unpack the list before sending it, so it can be recieved by the function as a separate variable.

def unpack(a,b):
    print(a)
    print(b)

l = ["Mango", "Banana"] #   we can unpack tuple also

unpack(*l)


#kwargs
# Used for passing keyworded, variable-length argument dictionary to functions.
# write ** before giving argument to the function

def try_kwargs(**di):
    print(di)



try_kwargs(name= "Umair",age=23)  # only this format can be used to give arguments as kwargs


# unpacking

def try_unpack(a,b):
    print(a)
    print(b)
  
    
   

d = {'a': 'Umair', 'b': 23}  # key must be same as argument given to the function

try_unpack(**d)