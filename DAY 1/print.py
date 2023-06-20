# print takes 5 parameters
# print(object= separator= end= file= flush=)

print("New Year", 2023, "Welocome", sep='. ')
print(5)

print("How are you", end="")
print("Have a nice day!")

x = 6
y = 12

print("The value of x is: {} and the value of y is: {}".format(x,y))
print("The value of x is: {1} and the value of y is: {0}".format(x,y)) 
print(f"The value of x is: {x} and the value of y is:{y}")
print(3, flush=True)