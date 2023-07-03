class MyClass:
    def __init__(self, value):
        self._value = value

    def showValue(self):
        print(f" The value is: {self._value}")

    @property                # getter  : Encapsulation
    def ten_value(self):
        return self._value * 10
    
    @ten_value.setter
    def ten_value(self, newVlaue):
        self._value = newVlaue/10

        
    


obj = MyClass(10)
print(obj._value)
obj.showValue()

print(obj.ten_value)
obj.ten_value = 300
print(obj.ten_value)
print(obj._value)