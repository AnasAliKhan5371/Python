num=[1,2,3,4,5,6,7]

def squares(a):
    return a**2
ans=map(squares,num)
print(ans)
ans=list(map(squares,num))
print(ans)

def even(a):
    return a%2==0

ans=list(map(even,num))
print(ans)