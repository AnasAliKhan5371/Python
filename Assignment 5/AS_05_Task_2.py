l=[1,2,3,4,5,6,7,8,9,10]
print('Original list: ', l)
extract=[]
for i in range(0,5):
    extract.append(l[i])

print('Extracted first five elements: ',extract)
extract.reverse()
print('Reversed extracted elements: ', extract)