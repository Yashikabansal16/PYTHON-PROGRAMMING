#1.Write a Python function to find the maximum and minimum numbers from a sequence of numbers. 

def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


# Example usage
nums = [10, 25, 3, 45, 7, 18]

max_val, min_val = find_max_min(nums)

print("Maximum:", max_val)
print("Minimum:", min_val)