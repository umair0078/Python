# Immutable

t = ('Umair',1,2,3)
print(t)

t1 = () # Empty Tuple
print(t1)

t2 = (1)  # it is integer not a tuple
print(t2)
print(type(t2))

t3 = (4,)  # Tuple with single value must contain a comma

print(t3)
print(type(t3))


# Tuple Methods

r = t.count(1)
print(r)

i = t.index(3)

print(i)
