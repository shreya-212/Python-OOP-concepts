class Student:
    def __init__(self,name,age):
        self.__age=age
        self.name=name
    
    def get_age(self):
        return self.__age
    
    def set_age(self,new_age):
        if new_age >0:
            self.__age=new_age
        else:
            print("Invalid age")

s1=Student("Sara",20)
print("Name: ",s1.name)
print("Age:",s1.get_age())
s1.set_age(21)
print("Updated age:",s1.get_age())
s1.set_age(-5)


