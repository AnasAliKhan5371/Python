# iterator
l=[1,2,3,4,5]
iteration=iter(l)
print(iteration.__next__())
print(iteration.__next__())
print(next(iteration))

# generator
def fun():
    yield 1
    yield 2
    yield 3

val=fun()
print(val.__next__())
for i in val:
    print(i)

# example
def squares():
    n=1
    while n<=5:
        s=n**2
        yield s
        n+=1
val=squares()
for i in val:
    print(i)