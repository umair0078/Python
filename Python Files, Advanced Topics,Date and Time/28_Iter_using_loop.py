numbers = [43, 4, 45, 3, 342, 1, 2]
# Iterate list using simple while loop
# index = 0
# while(index<len(numbers)):
#     print(numbers[index])
#     index += 1


# Iterate list using iterator with while loop
iter_obj = iter(numbers)

while (True):
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break

# for number in numbers:
#     print(number)