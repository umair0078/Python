import re

string = 'Hello 13 and 24 with 67'

pattern = '\d+'

result = re.findall(pattern, string)
print(result)


# 2nd Example
string = 'Ten:10 Seventy Eight:78.'
pattern = '\d+'

result = re.split(pattern, string,1) # maxsplit: 1
print(result)


# 3rd Example

string = '''abc 12\ 
de 23 \n f45 6'''

pattern = '\s+'
replace = ''

new_string = re.sub(pattern, replace, string)
print(new_string)


# 4th Example

string = '''abc 12\ 
de 23 \n f45 6'''

pattern = '\s+'
replace = ''

new_string = re.subn(pattern, replace, string)  # returns a tuple of 2 items containing the new string and the number of substitutions made.
print(new_string)


# 5th Example

string = 'Python Programming Language'

match = re.search('Python', string)

if match:
    print("Pattern Found inside the string")
else:
    print("Pattern not found")

# 6th Example

string = '54 565 5 34545 333'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'
match = re.search(pattern, string)

if match:
    print(match.group())
else:
    print("Pattern not found")

# 7th Example

string = '54 565 5 34545 333'

# Three digit number followed by space followed by two digit number
string = 'Hello, Have a nice day'
pattern = 'y$'
match = re.search(pattern, string)

print(match)