class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50


student1 = Student("Michał", [50, 80, 40])
student2 = Student("Natalia", [10, 20, 0])

print(student1.is_passed())
print(student2.is_passed())
