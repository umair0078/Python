# Dictionary as a set of counters

word = "standard-ad"
d = {}

for w in word:
    if w not in d:
        d[w] = 1
    else:
        d[w] = d[w] + 1

print(d)