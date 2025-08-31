class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._grade = {}
    
    def get_grade(self, key):
       return self.grade[key]
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, val):
        self._grade = val
    
    def set_grade(self, key, value):
        self._grade[key] = value

    def __str__(self):
        return f"The sudent name is {self.name} and age is {self.age} and the grade from all subjects is {self.grade}"
    
    def __len__(self):
        return len(self.grade)
    
    @property
    def average(self):
        total = 0
        for val in self.grade.values():
            total += val
        return total / len(self.grade)