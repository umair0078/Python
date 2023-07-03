list_of_numbers = [3, 6, 9, 12]
# print(dir(list_of_numbers))  # gives the all methods that could be apply on a list

Iterator = list_of_numbers.__iter__()

item1 = Iterator.__next__()
print(item1)

item2 = Iterator.__next__()
print(item2)

item3 = Iterator.__next__()
print(item3)

item4 = Iterator.__next__()
print(item4)

# To Write the clean code use:
numbers = [2,4,6,8]

Iterator = iter(numbers)

item1 = next(Iterator)
print(item1)

item2 = next(Iterator)
print(item2)

item3 = next(Iterator)
print(item3)

item4 = next(Iterator)
print(item4)