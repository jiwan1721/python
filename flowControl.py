# Flow control - control the flow of the progrm

# 1. if statement
# 2. if else statement
# 3. if else if statement
# 4. nested if


#indentation rule in python
# one tab or 4 white space
# 1. if statement - if we need to check single condition at a time
# syntax
# if condition:
#      expression


'''x = 6
if x!= 6:
    print("False")

if  x == 6:
    print("True")

text = "hello world"
if text is "heello world":
    print("True")

if text is not "Hello world":
    print("false")
# 2. if else - to check single condition with alternative expresion
# implementing input with if else statement

name = str(input("Enter your name: "))

# note - sometimes identity operator does not on input case to check identical value
# so we have to use == insted of is


if name == "PYTHON":
    print("Access Given")
else:
    print("Access Denied")'''

# 3. if else if statement - to check multiple condition or single condition multiple times
# syntax
# if condition:
#   expression
# elif condition:
#    expresssion

#syntax
#if condition:
#  expression
#elif condition:
#   expression
#elif condition:
#   expression
#else:
#    expression

day = "Monday"
if day =="sunday":
    print("is first day of week")
elif day == "Monday":
    ("second day of weel")
day_name = input("Enter the day name: ")
if day_name == "sunday":
    print(day_name,"first day of week")
elif day_name == "monday":
    print(day_name,"first day of week")
elif day_name == "tuesday":
    print(day_name,"is 2nd day of week")
elif day_name == "sunday":
    print(day_name,"is 3rd day of week")
elif day_name == "wednesday":
    print(day_name,"is 4th day of week")
elif day_name == "thrusday":
    print(day_name,"is 5th day of week")
elif day_name == "friday":
    print(day_name,"is 6th day of week")
elif day_name == "saturday":
    print(day_name,"is 7th day of week")
else:
    print("please enter correct day name")

# nested if statement - if statement inside the if statement
#syntax
#if condition:
#  if condition:
#     expression
#  else:
#      expression
#else:
#  expression


#syntax
#if condition:
#  if condition:
#     expression
#     if condition:
#        expressiom
#      else:
#         expression
#  elif:
#      expression
#else:
#  expression
code = 5544
email = "chandjiwn9@gmail.com"

if code == 5544:
    if email == "chandjiwn9@gmail.com":
        print("welcome")
    elif email == "chandjiwn@gmail.com":
        print("welcome2")
    else:
        print("check email")
else:
    print("check code")


#example num 2
if code == 5544:
    session = "5544"
    if email == "valve@stem.steam.com":
        if session == "5544":
            print("welcome one")
        else:
            print("return back")
    elif email == "chandjiwn9@gmail.com":
        print("welcome2")
        if session == "5544":
            print("welcome two")
        else:
            print("return back")
    else:
        print("check your email")
else:
    print("check code")

# task - use if statement, if else statement , if elif statement


































































































