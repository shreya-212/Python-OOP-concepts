class Employee:
    def __init__(self,role,dep,sal):
        self.role=role
        self.dep=dep
        self.sal=sal

    def showDetails(self):
        print("role=",self.role)
        print("dep=",self.dep)
        print("salary=",self.sal)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75000")
        
# e1=Employee("Accountant","Finance","21000")
# e1.showDetails()

eng1=Engineer("Elon",40)
eng1.showDetails()