#object Oriented Programming
x=lambda a: a+10
print(x(20))

class Car:
    h=10
    w=20
maruti=Car()
print(maruti.h)
print(maruti.w)


class  student:
    def __init__(st,name,reg):
        st.name=name
        st.reg=reg
obj =student("Murali",12219353)
print(obj.name)
print(obj.reg)
 
class  student:
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def pr(self):
        print("hello my name is " +  self.name)
obj=student("Murali",12219353)
obj.pr()
