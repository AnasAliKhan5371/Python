# tuples are immutable
n=(1,2,3,4,5)
print(n)
print(n[1])

# concatination
t1=('mike',10,2.5)
t2=('pop',1)
print(t1+t2)

# length
print(len(t1))

# immutable
'''
n=(1,2,3,4,5)
n[0]=9
print(n)
'''

# sorting
t=(2,3,4,7,6,34,26,99,0,1000)
sort=sorted(t)
print(sort)

# index
print(t.index(0))
print(t[-3])