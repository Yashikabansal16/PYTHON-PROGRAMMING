# take input from the user
n = int(input("Enter a number: "))

# initialize the factorial to one
fact = 1

for i in range(1,n+1):
    fact = fact * i

# print the result
print("The factorial of",n,"is",fact)