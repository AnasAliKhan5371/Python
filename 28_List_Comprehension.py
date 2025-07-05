x=[]
for i in range(11):
    z=i**2
    x.append(z)
print(x)

# list comprehension
x=[i**2 for i in range(11)]
print(x)

# even numbers only
x=[i**2 for i in range(11)if (i**2 % 2==0)]
print(x)