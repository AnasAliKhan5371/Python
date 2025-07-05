dict1={'Mike':66,'Nick':77,'Alice':85,'Joe':33}
name=input("Enter the student's name: " )
if name in dict1.keys():
    print("{}'s marks: {}".format(name,dict1[name]))
else:
    print('Student not found.')