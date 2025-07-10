def add(i,j):
    return (i+j)

def call(i,j):
    return add(i,j)   # return a function

def pas(i,j,fn):
    return fn(i,j)

a = add
b=a(1,2)
print(b)

c=call(1,2)
print(c)

d=pas(1,2,call)  #function as argument
print(d)