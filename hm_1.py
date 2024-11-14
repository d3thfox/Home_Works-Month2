class Person:
    def __init__(self,full_name,age,is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
    def intoduce_myself(self):
        print(f"NAME : {self.full_name}, AGE : {self.age}, MARRIED : {self.is_married}")
class Student(Person):
    def __init__(self,full_name,age,is_married,marks : dict):
        super().__init__(full_name,age,is_married)
        self.marks = marks
    def set_average_rating(self):
        average_rating = sum(self.marks.values())//len(self.marks)
        return average_rating
class Teacher(Person):
    base_salry = 30000
    def __init__(self,full_name,age,is_married,experience):
        super().__init__(full_name,age,is_married)
        self.experience = experience
    def set_salry(self):
        bonus = self.base_salry // 20
        experience_bonus = self.experience - 3
        salary = self.base_salry + experience_bonus * bonus
        return salary

def create_student():
    student1 = Student("Artem Peredyadko",16,False,{"math" : 5, "history" : 5,"geography" : 4})
    student2 = Student("Kovalenko Yaroslav", 18,False,{"math" : 3, "history" : 5,"geography" : 4})
    student3 = Student("Daniil Morozov",17,False,{"math" : 4, "history" : 3,"geography" : 4})
    studenst = [student1,student2,student3]
    return studenst
students = create_student()
for student in students:
    print(f"{student.full_name},AGE : {student.age},MARRIED :{student.is_married},{student.marks}")
    set_average_rating = student.set_average_rating()
    print(f"Average marks :{set_average_rating}")

teacher = Teacher("Rick Grimes",30,True,20)
print(f"{teacher.full_name} AGE : {teacher.age} MARRIED : {teacher.is_married} EXPIRY : {teacher.experience}")
salary = teacher.set_salry()
print(f"SALARY : {salary}")
























