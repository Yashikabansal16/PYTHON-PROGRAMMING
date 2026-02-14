'''8.Take two sets and apply various set operations on them :
S1 = {Red ,yellow, orange , blue }
S2 = {violet, blue , purple}'''


s1 = {'Red','Yellow','Orange','Blue'}
s2 = {'Violet','Blue','Purple'}

# various operations on sets
print("Intersection of s1 and s2: ",s1.intersection(s2))
print("Difference of s1 and s2: ",s1.difference(s2))
print("Union of s1 and s2: ",s1.union(s2))
print("Symmetric difference of s1 and s2: ",s1.symmetric_difference(s2))

