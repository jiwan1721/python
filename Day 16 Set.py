# Set - methods

# 1. add() - to add new element in set
days = {"Sunday", "Monday", "Tuesday"}
print("Set before: ", days)
days.add("Wednesday")
days.add("Thursday")
print("Set after: ", days)
print("\n")
days_list = ["Friday", "Saturday"]

for i in range(len(days_list)):
    days.add(days_list[i])

print("Set after loop: ", days)
print("\n")

# 2. copy() - copies or replicates all elements
# from one set to another set
days_copy = days.copy()
print("Set copied: ", days_copy)
print("\n")

# if the primary set if updated then there will
# be no impact on the copied set
days.add("Holiday")
print("Days updated: ", days)
print("\n")
print("Days copied: ", days_copy)
print("\n")


# 3 clear() - removes all element from the set

print("Set days: ", days)
print("\n")
days.clear()
print("Set days cleared: ", days)
print("\n")

# 4. pop() -removes random elements from the set
print("Days copy: ", days_copy)
days_copy.pop()
print("Days copy pop() 1: ", days_copy)
days_copy.pop()
print("Days copy pop() 2: ", days_copy)
days_copy.pop()
print("Days copy pop() 3: ", days_copy)
days_copy.pop()
print("Days copy pop() 4: ", days_copy)

days = days_copy.copy()
# throws error if the set is empty

# 5. removes - takes element as parameter and removes element from the set
# if the element is not available not throws error
print("Days re-copied: ", days)
days.remove("Monday")
print(days)


