# taking input from user
n = int(input("Enter a number: "))

# initialize sum to zero
sum = 0

for i in range(1,n+1):
    sum = sum + (1/i)

# display result
print("The sum of the series is: ",sum)

