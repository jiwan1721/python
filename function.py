#Function - to perform certain task repeatedly not for same instance, for future purpose

# function mst called by their name to execute their process
#types of function

# 1. Built in function/pre-defined function
# eg print(), input(), str(), int(), float()

# 2. user-defined function
# Types of user- defined function
# i. Return type with parameter
# ii. return type without parameter
# iii. Parameter with no return type
# iv. no parameter no return type

# syntax of function
# def function_name:
#     expression/function body

# Naming rule for defining/declaring function name
# 1.alphabetical character
# 2. no space between two or more words name
# 4. no use of special characters except underscore
# 5. case sensitive

# Naming case or convention - 1. came; case 3. pascal cse 3. Snake Case


def show():
    print("Hello World")
show()


# parameter - statement or expression passed between the paranthesis i.e smal bracket open-close
# 1. no return type and no parameter
print("no return type and no parameter")
def showResult():
    sum = 1+3
    print(sum)
showResult()

# 2. Return type with no parameter
print("Return type with no parameter")
def getPi():
    pi = 22/7
    return pi
print(getPi())

# 3.return type with parameter
print("return type with parameter")
def sum_of_Two_number(num_one, num_two):
    result = num_one + num_two
    return result
print("sum of two number: ",sum_of_Two_number(12,13))    

# 4. no return and with parameter
def area_of_triangle(base, height):
    area = 1/2*base*height
    print("Area of triangle: ", area)
area_of_triangle(12, 15)

# parameter vs argument
# parameter - defind variables inside the paranthesis while declaring function
# argument - assinged value to the variable of paranthesis while invoking/calling function 






































