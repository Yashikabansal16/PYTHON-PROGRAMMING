'''6.Write a lambda function which gives tuple of max and min from a list.
Sample input: [10, 6, 8, 90, 12, 56]
Sample output: (90,6)'''

find_max_min = lambda lst: (max(lst), min(lst))

# Sample input
numbers = [10, 6, 8, 90, 12, 56]

# Function call
result = find_max_min(numbers)

print(result)
