# taking input from user
n = int(input("Enter a number: "))

# initialize sum to zero
sum = 0

while n > 0:
     digit = n % 10
     sum = sum + digit
     n = n // 10

# display result
print("Sum of the digit is: ",sum)