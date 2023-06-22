from functools import reduce
l = [2,3,4,5,6,7]

def square(num):
    return num**2


for item in l:
    sq = square(item)
    print(sq)


# Square of all the numbers inside the list
sq_list = []

for item in l:
    sq_list.append(square(item))

print(sq_list)

# Square of all the numbers inside the list using list comprehension

squared_list = [item*item for item in l]
print(squared_list)

''' map,filter and reduce are built-in functions that allow you to appply a fuction to a sequence of elements(iterables)
 and return a new sequence.'''
# map, filter and reduce are higher order functions beacuse they takes function as an argument.
# synatax: map(function, iterable)
# map
l2 = [5,6,7,8,9]

m = map(square, l2) # first argument: a function and second argument: a list we want to map with that function
print(list(m))

m2 = map(lambda num: num**3, l)
print(list(m2))
# filter

def my_func(num):
    return num > 3

print(my_func(4)) # Output: True
print(my_func(2)) # Output: False

f = filter(my_func,l)
print(list(f))


def myfunc2(num):
    return num % 2 == 0

print(myfunc2(4))
print(myfunc2(3))

f2 = filter(myfunc2, l)
print(list(f2))

# filter by passing lambda function
f3 = filter(lambda num: num % 2 == 0, l)
print(list(f3))

# reduce
r = reduce(lambda a,b : a+b, l)
print(r)