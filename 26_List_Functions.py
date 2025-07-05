# add new value
from operator import index

l=['mike',10.1,1980]
l.append(10)
print(l)
l.extend([20,30,40])
print(l)
l.insert(2,'pop')
print(l)
print('\n')

# remove value
l.remove(10)
print(l)
l.pop(5)
print(l)
del l[1:4]
print(l)
l.clear()
print(l)
print('\n')

l=[10.1,1980,20,30,40]
# ascending
l.sort()
print(l)

# reverse
l.reverse()
print(l)

#index value
print(index(1980))

# length
print(len(l))

