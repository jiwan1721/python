# loop - to perform certain task repeatdly for certain period of time
# for loop
# syntax
# for value in sequence:
#    expression or loop body

num_list = [1,2,4,5,6,7,8,9,56,75]

# len() - is use to count the length of iterative object
print("lenght of list: ", len(num_list))
for num in num_list:
    print("numbers: ",num)

# range() with for loop
for i in range(10):
    print("Range value: ",i)
# len() and range together with for loop
for i in range(len(num_list)):
    print("list items' index: ",i)
    print("liat item by index: ",i,"value: ", num_list[i])
    
# else with for loop
item_list = ["box","tools","pins","Boards","cherry"]
for i in range(len(item_list)):
    print("index: ",i,"value: ",item_list[i])
else:
    print("no more items in the list")

#While loop
# syntax
# while expression:
#    body

# example
sum =0
num = 1
n = 10
while num<=n:
    sum = sum +num
    num+=1
print("the sum is: ", sum)

#below example will go infinite if we dont break the loop
num =1
while num>0:
    num+=1
    print("infinite",num)
    break


#while loop with else
sum =0
num = 1
n = 10
while num<=n:
    sum = sum +num
    num+=1
else:
    print("loop ended")
    

item_list = ["box","tools","pins","Boards","cherry"]
i =0
while i <=i in range(len(item_list)):
    print("index: ",i,"Value: ",item_list[i])
    i = i+1
else:
    print("No more items in list")
    























