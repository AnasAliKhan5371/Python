# r+
f=open('file_01.txt','r+')
f1=f.write('welcome')
print(f1)
f.close()

f=open('file_01.txt','r+')
f1=f.read()
print(f1)
f.close()