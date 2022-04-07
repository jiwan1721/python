# Dictionary
# 1. copy() - copies or replicates all items of primary dict to new dict
movie_detail = { 'id': 12, 'name': 'Kraken', 'genre': 'Sci-Fi', 'budget': '200M' }

# copying with copy method()
movie_detail_copy = movie_detail.copy()
print("Movie Details: ", movie_detail)
print("Movie Details Copy: ", movie_detail_copy)
print("\n")

# 2. clear() - removes all items from the dictionary
print("Movie Details Copy Before: ", movie_detail_copy)
movie_detail_copy.clear()
print("Movie Details Copy After: ", movie_detail_copy)
print("\n")

# 3. get()- takes key as parameter and return value of that particular
# key
print("Movie Details Key's value with get() method: ", movie_detail.get('name'))
print("\n")

# 4. items() - returns all keys along with values
print("Movie Details keys and values with items() method: ", movie_detail.items())
print("\n")

# 5. keys() - returns all keys from the dict
print("Movie Details keys with keys() method: ", movie_detail.keys())
print("\n")

# 6. values() - returns all values from the dict
print("Movie Details values with values() method: ", movie_detail.values())
print("\n")

# 7. pop() - takes specific key as parameter, removes specific key-value and return value
print("Movie Details Before: ", movie_detail)
print("Movie Details pop(): ", movie_detail.pop('budget'))
print("Movie Details After: ", movie_detail)
print("\n")

# throws KeyError if the key doesn't exist in the dictionary
# print("Non key:", movie_detail.pop('director'))

# 8. popitem() - by default removes the last inserted key-value and return key-value
# Based on the concept of LIFO - Last In - First Out

print("Movie Details Before: ", movie_detail)
print("Movie Details popitem(): ", movie_detail.popitem())
print("Movie Details After: ", movie_detail)
print("Movie Details popitem(): ", movie_detail.popitem())
print("Movie Details After: ", movie_detail)
print("Movie Details popitem(): ", movie_detail.popitem())
print("Movie Details After: ", movie_detail)
print("\n")

# throws KeyError if no item found in the dictionary
# print("Movie Details popitem(): ", movie_detail.popitem())

# 9. setdefault() - takes two 1. key 2. value as parameter and adds item to the dictionary
# if only passed one parameter i.e key then it takes value as None

# Case one: only key
print("Movie Detail Before: ", movie_detail)
movie_detail.setdefault('id')
print("Movie Detail After: ", movie_detail)
print("\n")

# Case two: key-value
print("Movie Detail Before: ", movie_detail)
movie_detail.setdefault('name','Lod of the Rings')
print("Movie Detail After: ", movie_detail)
print("\n")

# Case three: key exist - does nothing - no impact on the dict
print("Movie Detail Before: ", movie_detail)
movie_detail.setdefault('id')
print("Movie Detail After: ", movie_detail)
print("\n")

# Case four: key-value exist - does nothing - no impact on the dict
print("Movie Detail Before: ", movie_detail)
movie_detail.setdefault('id', 23)
print("Movie Detail After: ", movie_detail)
print("\n")

# 10. update() - takes iterable object and update the value of specified key
print("Movie Detail Before: ", movie_detail)
movie_detail.update({'id':23})
print("Movie Detail After: ", movie_detail)
print("\n")

# case multiple key-value object
print("Movie Detail Before: ", movie_detail)
movie_detail.update({'id':85, 'name': 'Spider Man - No way home'})
print("Movie Detail After: ", movie_detail)
print("\n")

# 11. fromkeys() - takes two parameter 1. iterable object 2. value
# if nothing passed as value then by-default value is None

# single valued value
name = ["id", "name", "price"]
value = "Hello"
result = dict.fromkeys(name, value)
print(result)

# multi valued value
name = ["id", "name", "price"]
value = ["1", "Tools", "300"]
result = dict.fromkeys(name, value)
print(result)
