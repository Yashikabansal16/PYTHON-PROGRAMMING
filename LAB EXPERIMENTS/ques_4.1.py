# 1.Write a program to count and display the number of capital letters in a given string.

# input string from user
str = input("Enter a string: ")

# initialize count to zero
count = 0

# count number of capital letters
for ch in str:
    if 'A' <= ch <= 'Z':
        count = count + 1
        
# display result
print("Total capital letters are: ",count)