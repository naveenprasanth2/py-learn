class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"The employee name is {self.name} with age is {self.age} and salary is {self.salary}"
    
    def __repr__(self):
        return f''''
        name is {self.name}
        age is {self.age}
        salary is {self.salary}
        '''
    
    def __add__(self, employee):
        return f"The combined name is {self.name} {employee.name} and age is {self.age + employee.age} and salary is {self.salary + employee.salary}"
    