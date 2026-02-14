#4.WAP to enter a string and a substring. You have to print the number of times that the
#substring occurs in the given string. String traversal will take place from left to right,
#not from right to left.
#Sample Input
#ABCDCDC
#CDC
#Sample Output
#2

# Input string and substring
s = input().strip()
sub = input().strip()

count = 0
sub_len = len(sub)

# Traverse string from left to right
for i in range(len(s) - sub_len + 1):
    if s[i:i+sub_len] == sub:
        count += 1

print(count)

