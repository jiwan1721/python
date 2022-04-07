# 1. Assignment Operator
# a. = eg. x = 5    equivalent to x= 5
# b. += eg. x += 5  equivalent to x = x + 5
# c. -= eg. x -= 5  equivalent to x = x - 5
# d. *= eg. x *= 5  equivalent to x = x * 5
# e. /= eg. x /= 5  equivalent to x = x / 5
# f. %= eg. x %= 5  equivalent to x = x % 5
# g. //= eg. x //= 5  equivalent to x = x // 5
# h. **= eg. x **= 5  equivalent to x = x ** 5
# i. += eg. x += 5  equivalent to x = x + 5

x = 5
x +=5
print(x)

y =9
y %=4
print(y)

# 3. Comparitive operator
#Greater than  >   eg.x>y
#smaller Than  <   eg.x<y
#Equal to   ==     eg. x==y
#Not equal to  !=  eg. x!=y
#Greater than equal to  >= eg. x>=y
#Smaller than equal to <=  eg. x<=y


x=6
y = 7
print(x<y)
print(x>y)
print(x==y)
print(x!=y)
print(x<=y)


# 4. logical operator
# and = true if both operands are true           x and y
# or = true if both either of operand is true    x or y
#not = true if operand is false
x = 7
y = 9
z = 9
print(x and y)
print(y and z)
print(x  or y)
print(x ==y and y ==z)
print("new", not x ==y and y ==z)
print(x ==y or y ==z)

# 5. Bitwise operator
#  & Bitwise and   x & y =0
# |  Bitwise  or   x | y = 14
# ~  Bitwise  NOT  ~x=~~11
# ^  Bitwise  XOR  x^y = 14
# >> BItwise right shift  x>>2=2
# << Bitwise left shift  x>>2=2

#. Identity Operator -to check identical value of non-iterative variable or object
# is - if identical return true
# is not - if not identical then return true

print("identity Operator")

name = "rukum"
name1= "dang"
name2="rukum"
name3="Rukum"
print(name is name1)
print(name is name2)
print(name2 is name3)
print(name is not name2)
print(name is not name1)

# does't work on iterative object
x = [1,2,3]
y = [1,2,3]
print("numbers: ",x is y)

#7. Membership Operator - to check whether the value or variable is found in the sequence or not
#iterative Object -> string, list, tuple, dict,set
 # 1. in - if value/vriable found true
 # 2. not in - if value/variable not found true


list_one = ['hello','world']
name ='hello world'
item = {'name': "hello world"}


print("list check")
print('hello' in list_one)
print('hello'not in list_one)

print("String check")
print('h' in name)
print('h'not in name)

print("Dict check")
print('name' in item)
print('hello' not in item)

print('hello' in item)
print('hello' not in item)




















































