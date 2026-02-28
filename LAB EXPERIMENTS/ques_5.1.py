# 1.Scan n values in range 0-3 and print the number of times each value has occurred.

n = int(input("Enter number of values: "))

count = [0, 0, 0, 0]   # For values 0,1,2,3

print("Enter values between 0 and 3:")

for i in range(n):
    value = int(input())

    if 0 <= value <= 3:
        count[value] += 1
    else:
        print("Invalid input! Enter value between 0 and 3.")
        
print("\nOccurrences:")
for i in range(4):
    print(f"{i} occurred {count[i]} times")
    
    