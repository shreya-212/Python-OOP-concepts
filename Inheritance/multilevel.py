#Multilevel inheritance
class Employee:
    def __init__(self,name):
        self.name=name
    
    def show_name(self):
        print(f"Employee name: {self.name}")

class Manager(Employee):
    def __init__(self,name,department):
        super().__init__(name)
        self.department=department
    
    def show_department(self):
        print(f"Department: {self.department}")

class Director(Manager):
    def __init__(self,name,department,level):
        super().__init__(name,department)
        self.level=level
    
    def show_level(self):
        print(f"Director level: {self.level}")
    
d=Director("ABC","IT","Senior")
d.show_name()
d.show_department()
d.show_level()