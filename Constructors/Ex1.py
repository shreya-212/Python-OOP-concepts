class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
    def display(self):
        print(f"Name: {self.name}, Rollno:{self.rollno}")
student1=Student("ABC",145)
student1.display()
    
