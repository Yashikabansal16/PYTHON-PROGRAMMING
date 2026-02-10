# take input from user
num = int(input("Enter a number: "))

# initialize first two numbers in fibonacci series
a = 0
b = 1

print("Fibonacci series: ")
for i in range(num):
    print(a,end=" ")
    a, b = b, a + b


