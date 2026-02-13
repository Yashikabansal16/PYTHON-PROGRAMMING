#2.Count total number of vowels in a given string.

# enter input from user
str = input("Enter a string: ")

# intilaize count to zero and define vowels
count = 0
vowels = "AEIOUaeiou"

# count number of vowels
for ch in str:
    if ch in vowels:
        count = count + 1

# display result
print("The number of vowels are: ",count)
