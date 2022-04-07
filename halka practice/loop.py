num_list = [1,2,3,45,5,4,67,5]
for num in num_list:
	print(num)
for i in range(10):
	print(i)

for i in range(len(num_list)):
	print(i)
	print("range: ",i,"numbers: ", num_list[i])

item_list = ["cherry", "banana", "rock"]
for i in range(len(item_list)):
	print("index: ",i,"value: ",item_list[i])
else:
	print("no more item left")


# while loop
sum = 0
num = 1
n = 10
while num<=n:
	
	num += 1
	sum = sum + num
	print("the sum is",sum)

else:
		print("loop ended")

