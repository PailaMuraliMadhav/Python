

def sum(x,y,z=0):
    return x+y+z
print(sum(2,3))
print(sum(2,3,4))

#polymorphism-multiple forms  of class

class Bird():
    def intro(self):
        print("This is a bird class")

    def flight(self):
        print("Bird fly")

class Parrot(Bird):
    def flight(self):
        print("Parrot can fly")
class Ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")

obj1= Bird()
obj2= Parrot()
obj3= Ostrich()

obj1.intro()
obj1.flight()

obj2.intro()
obj2.flight()

obj3.intro()
obj3.flight()

