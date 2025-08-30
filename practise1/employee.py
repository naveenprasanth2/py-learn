class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, object):
        if isinstance(object, Employee):
            return self.name + object.name + str(self.age + object.age)
        raise TypeError("Please send the valid type please...")
