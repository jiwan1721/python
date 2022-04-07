# Tuple
# 1. count() - takes value as parameter and counts the occurences of the
# value
days = ('Sunday', 'Monday', 'Monday', 'Tuesday', 'Wednesday')
print(days.count('Monday'))
print(days.count('Sunday'))

# if value doesnot exist - returns zero
print(days.count('Thursday'))


# 2. index() - takes value as parameter and returns index number of
# that value
print('Index Number of Sunday: ', days.index('Sunday'))
print('Index Number of Sunday: ', days.index('Monday'))
print('Index Number of Sunday: ', days.index('Tuesday'))
print('Index Number of Sunday: ', days.index('Wednesday'))
# if value doesnot exist - throws ValueError
# print('Index Number of Sunday: ', days.index('Thursday'))

