# String Methods
# 1. capitalize() - takes no parameter and returns first character as Uppercase and
# remaining as Lowercase of the particular string
print("Capitalize Method")
quote = "FAKE IT UNTIL YOU MAKE IT."
print(quote.capitalize())
quote_1 = "DONT BUILD A CASTLE IN THE AIR. QUOTES DAILY"
print(quote_1.capitalize())

# 2. casefold() - returns all characters to lower case and specially used to convert some
# special characters that are combined with two or more letters in english
# takes no parameter
print("Casefold Method")
german_word = "der Fluß"
print(german_word.casefold())
lower_case = "HELLO"
print(lower_case.casefold())

# 3. lower() - returns all characters to lower case
# takes no parameter
print("Lower Method")
name = "KATHMANDU, NEPAL"
print(name.lower())

# 4. uppper() - returns all characters to upper case
# takes no parameter
print("Upper Method")
name = "Hello. How are you my friend?"
print(name.upper())

# 5. center(self, width, character) - takes two paramater 1. width 2. string character
# here self is not counted as parameter
# if no characters are passed in second parameter then it takes space as default value
print("Center Method")
message = "Welcome to Mind Risers"
print("Without center method\n", message)
print("Without center method\n", message.center(50, '*'))
print("Without center method\n", message.center(50, ' '))

# 6. count() - takes one parameter and counts the number of occurences
# of the sub-string in the main string
# sub-string - part of string
print("Count Method")
quote = "Morning shows the day"
print(quote.count("o"))
print(quote.count("or"))
print(quote.count("tough"))

# 7. endswith() - takes one parameter which is suffix of the primary
# string and returns true if the suffix occurs at the end of the string
print("Endswith Method")
email = "mindrisers@edu.com.np"
# method one - defining substring
sub_string = "edu.com.np"
print("Defining substring: ", email.endswith(sub_string))
# method two - direct passing substring
print("Direct passing substring: ", email.endswith("gmail.com"))

# Task:- use if elif else statement and check string using endswith method

# 8. startswith() - takes one parameter which is prefix of the primary
# string and returns true if the prefix occurs at the beginning of the string
print("Startswith Method")
hotel_name = "5Start Annapurna"
print(hotel_name.startswith("5Star"))



