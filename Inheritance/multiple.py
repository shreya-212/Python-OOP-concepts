class Employee:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(f"Employee name: {self.name}")
    
class Salary:
    def __init__(self,salary):
        self.salary=salary
    def show_salary(self):
        print(f"Salary: {self.salary}")
    
class Manager(Employee,Salary):
    def __init__(self,name,salary,department):
        Employee.__init__(self,name)
        Salary.__init__(self,salary)
        self.department=department
    def show_details(self):
        print(f"Department:{self.department}")

m=Manager("ABC",10000,"IT")
m.show_name()
m.show_salary()
m.show_details()
