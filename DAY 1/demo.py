class Person:
    def __init__(self,time,marks):
        self.time = time
        self.marks = marks

    def info(self):
        if self.time>10:
            self.marks = self.marks + self.marks*(2.5/100)


    
Umair = Person(11,70)
print(Umair.marks)
Umair.info()
print(Umair.marks)


            

