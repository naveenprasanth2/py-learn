from employee import Employee

employee1 = Employee("naveen", 20, 10000.00)

employee2 = Employee("prasanth", 30, 10000.00)


print(employee1 + employee2)

def test(a : int , b : int) -> int:
    return a + b


if __name__ == '__main__':
    print(test(1, 2))
    