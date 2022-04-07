# Set Continue
# discard() - takes element as parameter and removes it
# from the set if its available

set_fruit = {"Apple", "Banana", "Orange", "Guava", "Pear"}

# if element is available - removes element
print("Fruits Before: ", set_fruit)
set_fruit.discard("Apple")
print("Fruits After: ", set_fruit)
print("\n")

# if element is not available - do nothing
print("Fruits Before: ", set_fruit)
set_fruit.discard("Pineapple") 
print("Fruits After: ", set_fruit)
print("\n")

# remove() - takes element as paramter and removes it from
# the set and the element must be a member of the set
# otherwise it will throw error
set_books = {"JAVA E1", "Hamlet", "Muna Madan", "Macbedth"}

# must be a member
print("Books before: ", set_books)
set_books.remove("JAVA E1")
print("Books after: ", set_books)

# if not member
print("Books before: ", set_books)
# set_books.remove("JAVA E1")
print("Books after: ", set_books)
print("\n")

# union() - returns new set of two sets are union to each
# other

set_places = {"KTM", "BKT", "BRT", "PKR", "DRN"}
set_cities = {"ITR", "DMK", "BWL", "HTD", "BM"}

print("Places before: ",  set_places)
print("Cities before: ",  set_cities)
new_set = set_places.union(set_cities)
print("Union Set: ", new_set)
print("Places after: ",  set_places)
print("Cities after: ",  set_cities)

# update() - takes set as a parameter and update it to
# existing primary set

even = [0, 2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9, 11]

# type casting list to set
set_odd = set(odd)
set_even = set(even)

print("Odd Before: ", set_odd)
print("Even Before: ", set_even)
set_odd.update(set_even)
print("Odd After: ", set_odd)
print("Even After: ", set_even)

# isdisjoint() - returns true if the sets are not intersect
even = [0, 2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9, 11]

# type casting list to set
set_odd = set(odd)
set_even = set(even)

print(set_odd.isdisjoint(set_even))

# if are intersect then return false
even = [0, 2, 4, 6, 8, 10]
odd = [1, 2, 3, 5, 7, 9, 11]

# type casting list to set
set_odd = set(odd)
set_even = set(even)

print(set_odd.isdisjoint(set_even))
print("\n")
# issuperset() - returns true if the set is a primary set
whole = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
even = {2, 4, 6}
print(whole.issuperset(even)) # true
print(even.issuperset(whole)) # false
print("\n")

# issubset() - returns true if the set is a child set
whole = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
even = {2, 4, 6}
print(whole.issubset(even)) # false
print(even.issubset(whole)) # true
