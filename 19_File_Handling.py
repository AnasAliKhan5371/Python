f=open('file_01.txt','r')
f1=f.read()
print(f1)
f.close()

f=open('file_01.txt','r')
f1=f.read(5)
print(f1)
f.close()

f=open('file_01.txt','r')
f1=f.readline()
print(f1)
f.close()

f=open('file_01.txt','r')
f1=f.readlines()
print(f1)
f.close()

with open('file_01.txt','r') as f:
    f1 = f.read()
    print(f1)
    f.close()



