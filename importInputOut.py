#pip - to include or import certain python packages or modules in the program or project
#namespace
#import keyword is use to import modules or packages
#import codes are written at the top of the progrm
import math
import os
print(math.pi)
print(math.atan2)

print(os.path)

#input output = takinginputs fromuser
#cace-int /basic input
number = input("enter a number: ")
print(number)

#case - restrict with type conversion
number_1 = int(input("enter first number: "))
number_2 = int(input("enter second number: "))
num = number_1+number_2
print(number_1)
print(number_2)
print(num)

#float
price = float(input("Enter item price: "))
print("price of item: ",price)

#string
first_name = str(input("enter your first name: "))
last_name = str(input("Enter your last name: "))
print("my name is", first_name, last_name)
