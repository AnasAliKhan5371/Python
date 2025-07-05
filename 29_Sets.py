# no duplicate elements
s={1,2,3,4,5}
print(s)
s={1,2,3,4,5,1}
print(s)

# add & delete
s={1,2,3,4,5}
s.add(6)
print(s)
s.remove(4)
print(s)

# in (check element)
print(2 in s)
print(4 in s)

s1={1,2,3,4,5}
s2={2,3,5,7}
# intersection
print(s1 & s2)

# union
print(s1.union(s2))

# subset
s1={1,2,3,4,5}
s2={2,3,4}
print(s2.issubset(s1))