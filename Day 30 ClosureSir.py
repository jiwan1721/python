# Closure
def getDetails():
    name = "Local"
    def inner():
        nonlocal name
        name = "Inner"
        return name
    inner()
    return name


print(getDetails())

# nonlocal variable -> variables that are defined out of the scope (global and local)
# we use nonlocal keyword to define variable nonlocal
x = "Hello"
def show():
    x = "Kathmandu"
    return x
print(show())

# Closure
def print_msg(msg):
    # this is a outer enclosing function
    def printer():
        # this is a nested function
        print(msg)
    return printer # returns the nested function

# calling out function
quote = print_msg("A day started with smile")
quote()

print(print_msg("Hello"))
del print_msg
quote()
try:
    print(print_msg("Hell"))
except:
    print("Function deleted")
quote()
# print_msg() function was called with message and returned function printer() was bound to
# another name or function i.e quote(). On calling quote(), the message was still remembered
# although the function print_msg() already finished executing.

# this type of technique by which some data i.e message gets attached to the code is
# called closure

# To have closure
# 1. must have nested function
# 2. nested function must refer to a value defined in the enclosing function
# 3. enclosing function must return nested function


