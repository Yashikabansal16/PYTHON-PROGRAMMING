'''8.Write a program to check whether all the values in a dictionary are same or not 
using lambda function.'''

# dictionary
d = {'a': 10, 'b': 10, 'c': 10, 'd': 10}

# lambda function to check values
check = lambda x: len(set(x.values())) == 1

# result
if check(d):
    print("All values are same")
else:
    print("Values are not same")