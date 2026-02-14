'''5.Given a string containing both upper and lower case alphabets. Write a Python program
to count the number of occurrences of each alphabet (case insensitive) and display the same.
Sample Input
ABaBCbGc
Sample Output
2A
3B
2C
1G'''

# Input string
s = input().strip()

# Convert to uppercase to make counting case-insensitive
s = s.upper()

# Get unique alphabets and sort them
unique_letters = sorted(set(s))

# Count and display occurrences
for ch in unique_letters:
    count = s.count(ch)
    print(count, ch, sep="")



