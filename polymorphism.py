class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def showcomplex(self):
        print( self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newreal=self.real+ num2.real
        newimg=self.img+ num2.img
        return Complex(newreal,newimg)
    
num1=Complex(2,3)
num1.showcomplex()
num2=Complex(1,2)
num2.showcomplex()

num3=num1+num2
num3.showcomplex()