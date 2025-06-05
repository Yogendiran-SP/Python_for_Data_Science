class Student(object):
    def __init__(self, name, age=18, grade=12):
        self.name = name
        self.age = age
        self.grade = grade
    def add_age(self,age):
        self.age = self.age+age
S1 = Student("Joshua", 17, 12)
# S1.add_age(5)
# print(S1.age)
add = S1.add_age
res = add(5)
print(S1.age)