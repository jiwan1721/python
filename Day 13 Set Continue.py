# 6. difference() - returns the remaining element from the primary set when two sets are differentiate to each other
# does no impact on any of the existing primary set
set_odd = {1, 3, 5, 7, 9}
set_even = {0, 2, 4, 6, 8}
set_even_copy = {0, 2, 4, 6, 8}
set_whole = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print("difference")
print("Before: ")
print("Even Number: ", set_even)
print("Odd Number: ", set_odd)
print("Whole Number: ", set_whole)
print("\n")
print("Whole Number - Even Number: ", set_whole.difference(set_even))
print("Whole Number - Odd Number: ", set_whole.difference(set_odd))
# if there are no items left in the primary set then returns empty set
print("Even Number - Even Copy: ", set_even.difference(set_even_copy))
print("After: ")
print("Even Number: ", set_even)
print("Odd Number: ", set_odd)
print("Whole Number: ", set_whole)
print("\n")

# 7. difference_update() - same as difference() but doesn't return any
# element and does impact on any of the existing primary set that means
# removes the match element from the primary set
print("difference_update")
print("Before: ")
print("Even Number: ", set_even)
print("Odd Number: ", set_odd)
print("Whole Number: ", set_whole)
print("\n")
print("Whole Number - Even Number: ", set_whole.difference_update(set_even))
print("Whole Number: After Even number difference", set_whole)
print("Whole Number - Odd Number: ", set_whole.difference_update(set_odd))
# if there are no items left in the primary set then returns empty set
print("Even Number - Even Copy: ", set_even.difference_update(set_even_copy))
print("After: ")
print("Even Number: ", set_even)
print("Odd Number: ", set_odd)
print("Whole Number: ", set_whole)
print("\n")

# 8. symmetric_difference() - returns the remaining element from both set when they
# are differentiate to each other
set_A = {1, 3, 5, 7, 9, 11, 13, 15} # Odd number
set_B = {0, 2, 4, 6, 8, 10, 12, 14} # Even number
set_B_copy = {0, 2, 4, 6, 8, 10, 12, 14} # Even Copy
set_C = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # whole number
print("symmetric_difference")
print("Before: ")
print("Set A: ", set_A)
print("Set B: ", set_B)
print("Set C: ", set_C)
print("\n")
print("Set C - Set A: ", set_C.symmetric_difference(set_A))
print("Set C - Set B: ", set_C.symmetric_difference(set_B))
# if there are no items left in the primary set then returns empty set
print("Set B - Set B Copy: ", set_B.symmetric_difference(set_B_copy))
print("After: ")
print("Set A: ", set_A)
print("Set B: ", set_B)
print("Set C: ", set_C)
print("\n")

# 9. symmetric_difference_update() - removes all element matching elements from
# primary set and keeps remaining element from both set when they
# are differentiate to each other
set_A = {1, 3, 5, 7, 9, 11, 13, 15} # Odd number
set_B = {0, 2, 4, 6, 8, 10, 12, 14} # Even number
set_B_copy = {0, 2, 4, 6, 8, 10, 12, 14} # Even Copy
set_C = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # whole number
print("symmetric_difference_update")
print("Before: ")
print("Set A: ", set_A)
print("Set B: ", set_B)
print("Set C: ", set_C)
print("\n")
print("Set C - Set A: ", set_C.symmetric_difference_update(set_A))
print("Set C: After Set A difference", set_C)
print("Set C - Set B: ", set_C.symmetric_difference_update(set_B))
# if there are no items left in the both set then returns empty set
print("Set B - Set B Copy: ", set_B.symmetric_difference_update(set_B_copy))
print("After: ")
print("Set A: ", set_A)
print("Set B: ", set_B)
print("Set C: ", set_C)
print("\n")

# 10. intersection() - returns all matching element from both set when they
# are intersect to each other

set_A = {1, 3, 5, 7, 9, 11, 13, 15} # Odd number
set_B = {0, 2, 4, 6, 8, 10, 12, 14} # Even number
set_C = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # whole number
print("intersection")
print("Before: ")
print("Set A: ", set_A)
print("Set B: ", set_B)
print("Set C: ", set_C)
print("\n")
print("Set C - Set A: ", set_C.intersection(set_A))
print("Set C - Set B: ", set_C.intersection(set_B))
# if there are no matching items left in the primary set then returns empty set
print("Set B - Set A: ", set_B.intersection(set_A))
print("After: ")
print("Set A: ", set_A)
print("Set B: ", set_B)
print("Set C: ", set_C)
print("\n")

# 11. intersection_update() - removes all unmatch elements from both set
# and keeps all matching element to the primary set from which the set
# was intersect
set_A = {1, 3, 5, 7, 9, 11, 13, 15} # Odd number
set_B = {0, 2, 4, 6, 8, 10, 12, 14} # Even number
set_C = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # whole number
print("intersection")
print("Before: ")
print("Set A: ", set_A)
print("Set B: ", set_B)
print("Set C: ", set_C)
print("\n")
print("Set C - Set A: ", set_C.intersection_update(set_A))
print("Set C: After Set A intersect", set_C)
print("Set C - Set B: ", set_C.intersection_update(set_B))
# if there are no matching items left in the primary set then returns empty set
print("Set B - Set A: ", set_B.intersection_update(set_A))
print("After: ")
print("Set A: ", set_A)
print("Set B: ", set_B)
print("Set C: ", set_C)
print("\n")



