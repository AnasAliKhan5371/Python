#Strings are mutable -----> can be changed

num = [1,2,3,4,5]
print(num[3])
print(num)

colors=['black','red','white','blue']
print(colors[2])

mix=['peter',10,'sam',50]
print(mix[2])

blank=[]
print(blank)
print('\n')

# Concatination
l1=['mike',10.1,1980]
l2=['pop',1]
print(l1+l2)
l1.extend(l2)
print(l1)

# edit
l1[0]='hardwork'
print(l1)

# multiply
n=[1,2,3,4]
print(n*2)

# in
game=['football', 'cricket', 'basketball']
print('tennis' in game)