# Set is an unordered collection of unique items. It is unindexed
# We cannot repeat values in a set
s = {"Umair",1,2,3,4,44,4,4,2,1,1,(1,2)} # We cannot add unhashable list or dictionary to a set but we can add hashable tuple

print(s)

# Empty Set

s1 = {} # It will create a empty dictionary not a empty set

print(s1)
print(type(s1))

# Creating Empty Set

empty_set = set()

print(empty_set)
print(type(empty_set))

# set methods
se = {1,2}
se.add(3)
se.add(3)
se.add("3")
print(se)

# Cannot add list or dictionary to sets

# se.add({"key":"value"})
# print(se)

print(s)

s.remove("Umair")
print(s)
s.remove(1)
print(s)
s.pop()
print(s)

# Important

new = {7,7.0,'7'}
print(new)
print(len(new))
