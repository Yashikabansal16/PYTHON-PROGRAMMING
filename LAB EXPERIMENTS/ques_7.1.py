total = vowel = 0
longest = ""

with open("name.txt") as f:
    for name in f:
        name = name.strip()
        total += 1
        
        if name[0].lower() in "aeiou":
            vowel += 1
        
        if len(name) > len(longest):
            longest = name

print("Total =", total)
print("Vowel =", vowel)
print("Longest =", longest)