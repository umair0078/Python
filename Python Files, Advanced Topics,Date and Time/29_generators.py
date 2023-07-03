# Generators are used to generate values on the fly instead of storing values in list,tuples and sets(Memory).
# Generators are lazy i.e., values are generated only when they are requested

def my_generator():
    for num in range(5):
        yield num

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for number in gen:
    print(number)