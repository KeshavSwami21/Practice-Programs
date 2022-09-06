# class Student:
#     def __init__(self,name,marks):
#         self.marks = marks
#         self.name = name
#     def show(self):
#         print(self.name,self.marks)


# obj = Student("Ram",100)
# print(obj.name)
# print(obj.marks)
# obj.show()


class Person:
    def __init__(xyz,name,age):
        xyz.name = name
        xyz.age = age

    def show(xyz):
        print(xyz.name,xyz.age)


class Child(Person):
    def __init__(xyz,name,age,phone):
        super().__init__(name,age)
        xyz.phone = phone

    def pr(xyz):
        print(xyz.name,xyz.age,xyz.phone)

obj = Child("ram",24,9888999728)
obj.pr()