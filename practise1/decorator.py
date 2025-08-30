class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def first_name(self):
        return self.name.split(" ").join("")
    
    @first_name.setter
    def first_name(self, first_name):
        self.name = f"{first_name} {self.name.split(" ")[1]}"


emp = Employee("naveen prasanth", 22)

print(emp.name)

emp.first_name = "summa"

print(emp.name)
