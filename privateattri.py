class Emp:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,new_salary):
        if new_salary>0:
            self.__salary=new_salary
            print(f"Salary updated for {self.name}")
        else:
            print("invalid salary amount")

    def __calculate_bonus(self):
        return self.__salary*0.10
    
    def get_salary_with_bonus(self):
        return self.__salary + self.__calculate_bonus()


p1=Emp("sara",12000)
print(p1.name)
print(p1.get_salary())

p1.set_salary(20000)
print(p1.get_salary())

print(p1.get_salary_with_bonus())
