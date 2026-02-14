'''7.Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
a)	Fruits which are in both sets s1 and s2
b)	Fruits only in s1 but not in s2
c)	Count of all fruits from s1 and s2'''
# input fruits from user
n = int(input("Enter number of fruits in each set: "))

# create set s1
s1 = set() # empty set
print("Enter fruits for s1: ")
for i in range(n):
    fruit = input()
    s1.add(fruit) # add fruit to set 1
    
# create set s2
s2 = set()
print("Enter fruit to s2: ")
for i in range(n):
    fruit = input()
    s2.add(fruit) # add fruit to set 2
    
# various operation on sets
common = s1.intersection(s2)
only_s1 = s1.difference(s2)
total_unique = len(s1.union(s2))

# display result of each operation
print("Fruits in both s1 and s2: ",common)
print("Fruits only in s1 but not in s2: ",only_s1)
print("Unique fruit count from s1 and s2: ",total_unique)



