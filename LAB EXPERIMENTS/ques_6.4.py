#4.Write a recursive function to print Fibonacci series upto n terms

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print Fibonacci series
n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")