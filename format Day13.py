#format
#case one - no variable or index
print("format method")
print("case one - no variablen or index")
print("hello! {}, well your room number is {}".format("Jiwan",45))
#case two - with index
print("case two = with index")
print("hello! {0}, well your room number is {1}".format("Jiwan",45))
#case three - with variable
print("case three = with variable")
print("hello! {name}, well your room number is {room}".format(name="Jiwan",room =45))
#case four - index and variable
print("case four = with index")
print("hello! {0}, well your room number is {room}".format("Jiwan",room=45))

#split()
print("split methode")
message = "hello everyone. Hope you are doing great and well."
#method one - defining sub string
sub_string ="o"
print(message.split(sub_string))
# method two - direct passiing sub string
print(message.split(" "))


#replace() - takes two parameter old substring and new substring
# that replace the old substring
