l = [4,1,3,8,5]

l.sort()
print(l)


l2 = l.copy()
print(l2)

l.reverse()
print(l)

l.append("Umair")
print(l)

l.insert(2, "Mango")
print(l)

l.pop(1) # removes item from 1st index
print(l)

l.remove("Mango")
print(l)

l.clear()

print(l)

# extends will add all the elements of iterables(list, tuple, string etc.) at the end of the list
x = [2,3]
y = (1,2,3,4,5,6,7,8,"Hello")

x.extend(y)

print('x =', x)

z = [5,6,7,(5,8)]

print(z)

x.extend(z)
print(x)
