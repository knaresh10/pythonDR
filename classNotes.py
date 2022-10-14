class Student:
    __group = "Aditya"
    def __init__(self,rollno,branch,college):
        self.rollno = rollno 
        self.branch = branch
        self.college = college
        self.group = "aditya"
    def display(self):
        print(self.rollno,self.branch,self.college)
        print(Student.__group)

s1 = Student(123,"cse",'AEC')
s1.display()
print(Student.__group)
