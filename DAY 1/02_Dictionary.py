d = {
    "name":"Umair",
    "age": 22,
     "li": [1,2,3],
     "tu": (1,2,3),
     "pc": {"RAM":16,
            "Brand":"Dell",
             7:68
            }

}

print(d)
print(type(d))

print(d["age"])

a = d["li"]
print(a)

d["age"] = 23
print(d)

print(d["pc"])
print(d["pc"][7])
print(d["pc"]["RAM"])

# Dictionary Methods

print(d.keys())

print(list(d.keys()))

print(list(d.values()))

print(d.items())  # Prints the (key, value) for all contents of the dictionary 

new_d = {
    8:88,
    "greetings":"Good Morning"
}

d.update(new_d)
print(d)

print(d.get("age")) # Prints value associated with key "age"
