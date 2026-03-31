nums = []

with open("numbers.txt") as f:
    for x in f:
        nums.append(int(x.strip()))

print("Max =", max(nums))
print("Average =", sum(nums)/len(nums))
print("Count > 100 =", sum(1 for i in nums if i > 100))