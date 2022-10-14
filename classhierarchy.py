class Personal:
    a = 200
    def __init__(self,name,phno):
        self.name = name
        self.phno = phno

    def display(self):
        print(self.name, self.phno)

class Student(Personal):
    def __init__(self,rollno,branch,name,phno):
        super().__init__(name,phno)
        self.rollno = rollno
        self.branch = branch

    def display(self):
        print(self.rollno, self.branch)
        super().display()


s = Student(123,'CSE','Naresh',1234567890)
s.display()
print(s.a)
