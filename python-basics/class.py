class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"{self.name} scored {self.marks}")

s1 = Student("Apoorva", 85)
s2 = Student("Sanjana", 90)
s1.show()   
s2.show()   
