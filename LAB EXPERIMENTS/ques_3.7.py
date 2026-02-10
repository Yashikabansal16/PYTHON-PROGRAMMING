# initialize count to zero
count = 0

print("Number divisible by 5 or 7 is: ")

# finding numbers
for i in range(1,101):
    if i % 5 == 0 or i % 7 == 0:
        print(i,end=" ")
        count = count + 1

# display result
print("\n Total count is:",count)


