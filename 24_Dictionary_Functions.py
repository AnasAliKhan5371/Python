dict1={'a':'apple','b':'ball','c':'cat','d':'dog'}
dict1['e']='elephant'
print(dict1)

# deletion
del(dict1['c'])
print(dict1)
print('\n')

# in & get() (check)
print('b' in dict1)
print('g' in dict1)
print(dict1.get('g'))
print(dict1.get('g',"'g' not found"))
print('\n')

# get all keys and values
print(dict1.keys())
print(dict1.values())
print('\n')

# length
print(len(dict1))

# looping over keys
for item in dict1.keys():
    print(item)

