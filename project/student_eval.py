from student import Student

student1 = Student("naveen", 20)
student1.set_grade("chemistry", 100)
student1.set_grade("maths" , 99)
student1.set_grade("physics" , 99)
student1.set_grade("social" , 98)

print(student1.average)
print(student1.grade)
print(len(student1))