n=[1,2,3,4,5,6,7]

def even(a):
    return a%2==0

ans=filter(even,n)
print(ans)
ans=list(filter(even,n))
print(ans)
ans=set(filter(even,n))
print(ans)
ans=set(filter(lambda a:a%2==0,n))
print(ans)
ans=set(filter(lambda a:a%2==0,range(1,11)))
print(ans)
