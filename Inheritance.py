# Inheritance
# Example :- shape, square, Rhombus, Quarddileteral, cuboid
# Example:- Person, Boy, Adult, Human, Male, Old Age,child
# Example:- Vehicle, car, Truck, Bus, Bike

#Example:-
class Person:
    name = str
    gender= str
    def walk(self):
        print("Person can walk")
    def breathe(self):
        print("Person can breath")
class Boy(Person):
    age = int
    def category(self):
        print("Under 18")
b1 = Boy()
b1.name = "Harry"
b1.gender = "Male"
b1.age = 12
print(b1.name)
print(b1.gender)
print(b1.age)
b1.walk()
b1.breathe()
b1.category()

p1 = Person()
p1.name = "jiwan"
p1.gender = "Male"
p1.walk()
print(p1.name, p1.gender)

# with constructor
# if constructor is defined inside child class then child class must define parent class
# constructor inside child class constructor
# two ways to define parent class constructor
# 1. By class name -> must pass self inside constructor
# 2. super() method
class Empolyee:
    category = str
    shift = str
    etype = str
    def __init__(self):
        self.category = "Admin"
        self.shift = "Morning_ Evening"
        self.etype = "Permanent"
    def getInfo(self):
        print(self.category)

        
class Receptionlist(Empolyee):
    # attributes -> adjective -> characters -> properties
    salary = float


    
    # __init__ -> special type of function which is used as a constructor in python
    # to create or build object. Class attributes are initialized inside constructor
    def __init__(self):
        Empolyee.__init__(self)
        self.salary = 25000.00

    # method -> class behaviour -> verb
    def details(self):
        print(self.category, self.shift, self.etype,self.salary)
        
r1 = Receptionlist()
r1.details()
# super() method
class ITOfficer(Empolyee):
    department = str
    def __init__(self):
        super().__init__()
        self.department = "IT"
    def info(self):
        print(self.category,self.shift, self.etype,self.department)

i1 = ITOfficer()
i1.info()
i1.getInfo()






























