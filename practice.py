import email


print("capatilize() method")
String1="FAKE IT UNTIL YOU MAKE IT"
print(String1.capitalize())
String2="FAKE IT UNTIL YOU MAKE IT.QUOTES DAILY"
print(String2.capitalize())


print("LOwer() method")
str1 = "JIWAN CHANDA"
print(str1.lower())

print("upper() method")
x = str1.lower()
print(x.upper())

print("\n")
print(x.center(20," "))

print("\n")
email = "jiwanchand@gmail.com"
#method defining substring
sub_string = "edu.com.np"
print(email.endswith(sub_string))

print(email.endswith("gmail.com"))