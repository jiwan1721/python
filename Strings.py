# String Methods
# 1. capitalize() - takes no parameter and returns first character as uppercase and remaining as lowercase of the particulat string
#remaining as lowercase of the particular string
quotes ="FAKE UNTIL YOU MAKE IT."
print(quotes.capitalize())
quote_1 = "DONT BUILD IN THE AIR .QUOTES DAILY"
print(quote_1.capitalize())

# 2. caseFold- returns all charcters to lower case and specially used to convert some
# special characters that are combined with two or more letters in english
#takes no parameter
print("caseFold Methode")
german_word = "der fluß"
print(german_word.casefold())

# 3. Lower() - returns all character to lower case
# takes no parameter
print("lower Method")
name = "RUKUM, NEPAL"
print(name.lower())

# 4. upper() - returns all character to upper case
# Takes no parameter
print("upper Method")
name = "Hello, How are you"
print(name.upper())

# 5. center(self, width, character) - takes two parameter 1. widdth 2. String character
# here self is not counted as parameter
# if no characters are passed in second parameter then it takes space as default values
print("Center Method")
message = "Welcome to my heart"
print("without center method\n",message)
print("withot center method\n",message.center(50,'*'))
print("Without center method\n", message.center(50,' '))

# 6. count() - takes one parameter and countss the number of occurences
# of thr sub-string in the main string
# sub-string - part of string
print("Count Method")
quote = "Morning shows the day"
print(quote.count("o"))
print(quote.count("or"))

# 7. endwith() - takes one parameter which is suffixof the primary
# string and returns rue if the suffix occurs or the end of the string
print("Endswith Method")
email = "jiwanchand@gmail.com"
# method one - definig substring
sub_string = "edu.com.np"
print("Defining  substring: ",email.endswith(sub_string))
# method two - direct passing subsring
print("Direct passing substring : ", email.endswith("gmail.com"))

































