'''9.Write a program to create two lists and 
generate a dictionary with keys from list1 and values from list2.'''

# create two lists
list1 = ['a', 'b', 'c', 'd']
list2 = [10, 20, 30, 40]

# generate dictionary
result = dict(zip(list1, list2))

# display dictionary
print("Dictionary:", result)