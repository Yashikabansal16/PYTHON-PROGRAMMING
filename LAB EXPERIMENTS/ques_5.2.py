#2.Create a tuple to store n numeric values and find average of all values.

n = int(input("Enter number of values: "))

values = []

print("Enter numeric values:")
for i in range(n):
    num = float(input())
    values.append(num)

numbers = tuple(values)   # Convert list to tuple

average = sum(numbers) / n

print("\nTuple:", numbers)
print("Average:", average)

