# If an employee comes office after 9:30 A.M, deduct 1.5% salary of that employee.
import datetime
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def deduct_if_late(self):
        arrival_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        time_deadline = datetime.time(9,30,0).strftime("%I:%M:%S %p")
        if arrival_time > time_deadline:
            self.salary = self.salary - (1.5/100)*self.salary



Asad = Employee("Asad",10000)

print(Asad.salary)
Asad.deduct_if_late()
print(Asad.salary)

Amjad = Employee("Amjad",20000)
print(Amjad.salary)

Amjad.deduct_if_late()
print(Amjad.salary)
