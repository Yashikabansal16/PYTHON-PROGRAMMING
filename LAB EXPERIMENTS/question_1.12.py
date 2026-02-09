a = [0,1]
b = [0,1]

# bitwise operators
print("A B A&B A|B A^B")
for x in a:
    for y in b:
        print(x,y," ",x&y," ",x|y," ",x^y," ")