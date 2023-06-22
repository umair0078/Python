# Python function to find maximum of three numbers

def max(num1,num2,num3):
    if num1 > num2:
        f = num1
    else:
        f = num2
    
    if f > num3:
        greater = f
    else:
        greater = num3

    return greater


m = max(10,30,100)
print(m)