f=open('output.txt','w')
a=input('Enter text to write to the file: ')
f1=f.write(a)
f2=f.write('\n')
print('Data successfully written to output.txt.')
f.close()

f=open('output.txt','a')
a=input('\nEnter additional text to append: ')
f1=f.write(a)
print('Data successfully appended.')
f.close()

f=open('output.txt','r')
print('\nFinal content of output.txt:')
f1=f.read()
print(f1)
f.close()