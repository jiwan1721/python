#datatypes
# list = collection of sequences of data with similar or diferent data types
#array = collectio of similar datatypes - python doesnt support array so list is used instaead of arary





even_number = [2,4,6,7,8,0]
print(type(even_number))
print(even_number)

#Float array
price_list = [1200.22, 150.123, 123.43]
print(type(price_list))
print(price_list)

#string array
name_list = ["jiwan", "ram", "hari", "krishna"]
print(type(name_list))
print(name_list)

#getting value of list with index number
# index of list always starts from zero
print("index 0",even_number[0])
print("index 1: ",even_number[1])

item_list = [1, "hello ", 456.66,"true"]
print(type(item_list))
print(item_list)



# tuple - collectio of constant data sequencees which are immutable
#mutable - changeable
# immutable - unchangeable
 # syntax
# variable_name = (,)
#variable_name = ("item1", "item", ..."nth item")

jiwan =("ram", "hari", "kssm")
print(type(jiwan))
print(jiwan)

#extra info about tuple declaratio
v_1 = 'a',
v_2 = 'a'
v_3 = ('a',)
print(type(v_1))
print(type(v_2))
print(type(v_3))

#dict - collection of datawith key - value pair and are mutable
#json - javascript object notation
#php - associative array
#syntax
#variable_name = {key:value,key:value}

places = {"name":"rukum","location":"Nepal"}
print(type(places))
print(places)


#set - collwction of unordered data which are mutable and unique
#syntax
#variable_name = {item1,item2...,nth item}

numbers = {2,3,4,5,4,4,5,5,4,4,3,6}
print(type(numbers))
print(numbers)

names = {"jiwan", "ram","jiwan","ram"}
print(type(names))
print(names)


#range()
#sybntax
#range(end)   # equivalent to range(0,end)
#range(start, end)
#range(start,end,step

#note = start must be smaller than end
print(*range(10)) # value output upto 0-1 or end-1
print(*range(4,25))
print(*range(2,30,5))





