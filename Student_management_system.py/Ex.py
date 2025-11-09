class Student:
    def __init__(self,name,rollno,age,course):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.course=course
    def __str__(self):
        return f"Name:{self.name} | Rollno:{self.rollno} |Age:{self.age} |Course:{self.course}"
    

class StudentManager:
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        for i in self.students:
            if i.rollno==student.rollno:
                print("Roll no already exists")
                return
        self.students.append(student)
        print("Student added successfully")
    
    def view_student(self):
        if not self.students:
            print("No students in system")
        else:
            for s in self.students:
                print(s)
            print()
    
    def Search_student(self,rollno):
        for s in self.students:
            if s.rollno==rollno:
                print("Student found",s)
                return
        print("No such student")
        
    def update_details(self,rollno):
        for s in self.students:
            if s.rollno==rollno:
                name=input("Enter name:")
                rollno=input("Enter rollno:")
                age=input("Enter age:")
                course=input("Enter course:")

                s.name=name
                s.rollno=rollno
                s.age=age
                s.course=course
                print("Student details updated successfully")
                return
        print("No such student")

        

    def delete_student(self,rollno):
        for s in self.students:
            if s.rollno==rollno:
                self.students.remove(s)
                return
        print("no such student")

def main():
    m=StudentManager()
    
    while True:
        print("----Student Managerment System----")
        print("1. Add student") 
        print("2. View student")
        print("3. Search student")              
        print("4. Update student")
        print("5.Delete student")
        print("6.Exit")
        try:
            choice=int(input("Enter a choice: "))
        except ValueError:
            print("Invalid choice")
            continue
        
        if choice==1:
            name=input("Enter name: ")
            rollno=input("Enter rollno: ")
            age=input("Enter age: ")
            course=input("Enter course: ")
            student=Student(name,rollno,age,course)
            m.add_student(student)

        elif choice==2:
            m.view_student()

        elif choice==3:
            rollno=input("Enter the rollno to be found: ")
            m.Search_student(rollno)
        
        elif choice==4:
            rollno=input("Enter the rollno to be updated: ")
            m.update_details(rollno)

        elif choice==5:
            rollno=input("Enter the roll no to be removed: ")
            m.delete_student(rollno)

        elif choice==6:
            print("Exiting")
            break
        else:
            print("Invalid choice number")
if __name__=="__main__":
    main()


            






    

