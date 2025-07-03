f=open('file_01.txt','w')
f1=f.write('hello')
print(f1)
f.close()

f=open('file_01.txt','r')
f1=f.read()
print(f1)
f.close()