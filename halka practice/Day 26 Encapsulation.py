# Encapsulation
# private -> can be access within the class
# public -> can be access anywhere
# protected -> can be access within the package

class Person:
    # private attribute
    __gender = str

    def __init__(self, param_name, param_age):
        # public attribute
        self.name = param_name
        
        # protected attribute
        self._age = param_age
        
    # access modifier 1. getter 2. setter -> must be public method
    # 1. getter ->  to access private properties value -> return type, no parameter
    # 2. setter -> to store values in private properties -> no return type, parameter

    def getGender(self):
        return self.__gender

    def setGender(self, param_gender):
        self.__gender = param_gender
        
p1 = Person("Ram Saran", 24)
print(p1.name)
print(p1._age)
p1.setGender("Female")
print(p1.getGender())




