def greet(name):
    print("Good Morning!", name)


def sum(a, b, c):
    s = a + b + c
    return "The sum is:", s

def square(num):
    sq = num*num
    return sq


greet("Umair")

s = sum(2,2,2)
print(s)

square_of_num = square(6)
print(square_of_num)



def get_square(num):
    square = num*num
    return f"The Square of {num} is {square}"

# calling the get_square function inside the for loop
for i in [1,2,3,4,5]:
    result = get_square(i)
    print(result)


# default arguments

def avg(a = 20, b = 5):
    average = (a + b)/2
    return average


a = avg(b=2, a=4)
print(a)


def info(fname, lname):
    fullname = f"Your name is: {fname} {lname}"
    return fullname


i = info("Muhammmad", "Umair")
print(i)

# Program to find sum of multiple numbers:

def sum_mul_num(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    return result
    

rs = sum_mul_num(1,2,3,4,5)
print(rs)