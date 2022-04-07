# Inheritance -> to inherit the base or parent class properties by the child class
# Example:- Shape, Square, Rhombus, Quardileteral, Cuboid
# Example:- Person, Boy, Adult, Human, Male, Old Age, Child
# Example:- Vehicle, Car, Truck, Bus, Bike

# Example:-
class Person:
    name = str
    gender = str

    def walk(self):
        print("Person can walk")

    def breathe(self):
        print("Person can breathe")
    
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
p1.name = "Minal"
p1.gender = "Male"
p1.walk()
print(p1.name, p1.gender)
# p1.category() -> cannot access the properties of another class directly without inheriting
# p1.age = 12

# with constructor
# if constructor is defined inside child class then child class must define parent class
# constructor inside child class constructor
# two ways to define parent class constructor
# 1. By class name -> must pass self inside constructor
# 2. super() method

class Employee:
    category = str
    shift = str
    emp_type = str

    def __init__(self):
        self.category = "Admin"
        self.shift = "Morning-Evening"
        self.emp_type = "Permanent"

    def getInfo(self):
        print(self.category)

# by class name
class Receptionist(Employee):
    # attributes -> adjective -> characters -> properties
    salary = float

    # __init__ -> special type of function which is used as a constructor in python
    # to create or build object. Class attributes are initialized inside constructor
    def __init__(self):
        Employee.__init__(self)
        self.salary = 25000.00

    # method -> class behaviour -> verb
    def details(self):
        print(self.category, self.shift, self.emp_type, self.salary)

r1 = Receptionist()
r1.details()

# super() method
class ITOfficer(Employee):
    department = str

    def __init__(self):
        super().__init__()
        self.department = "IT"

    def info(self):
        print(self.category, self.shift, self.emp_type, self.department)

i1 = ITOfficer()
i1.info()
i1.getInfo()

