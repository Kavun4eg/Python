class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}, Average_grade: {self.average_grade}"


student1 = Student("Slava", "Kaunenko", 27, 99)


print(student1)
student1.change_average_grade(100)
print(student1)