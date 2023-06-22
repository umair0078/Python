# lambda argument(s) : expression

greet = lambda : print("Good Morning!")

greet()

greet_person = lambda name : print("Good Morning", name)

greet_person("Umair")


double_num = lambda num : num*2

print(double_num(2))

cube = lambda num: num**3

print(cube(2))

# passing lambda function as an argument to the function

def calculate(func, value):
    return 2 + func(value)


c = calculate(lambda num : num*num, 2)
print(c)

# create another function
def calculate2(func, value1,value2):
    return 2 * func(value1,value2)

c2 = calculate2(lambda a,b: a+b, 2,3)

print(c2)