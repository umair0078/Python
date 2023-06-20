# 1. Implicit Type Conversion   => Automatic Type Conversion
# 2. Explicit Type Conversion   => Manual Type Conversion

# 1. Implicit Type Conversion

a = 5
b = 6.2
num = a+b

# Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.

print("Value:",num)  # Output => 11.0
print("Data Type:",type(num))

# 2.Explicit Type Conversion
x = 5.0

x = int(x)
print(x)
print(type(x))