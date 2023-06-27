# Recursive Factoral
def factorial(n):
    if n ==1 or n ==0:
        return 1
    else:
        fac = n * factorial(n-1)
        return fac
    

f = factorial(5)
print(f)

# Iterative Factorial
def itaerative_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i 
    return factorial
    


iter_fac = itaerative_factorial(4)
print(iter_fac)


