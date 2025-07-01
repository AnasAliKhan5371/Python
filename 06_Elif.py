a=int(input('Enter Operand 1: '))
b=int(input('Enter Operand 2: '))
op=input('Enter(+, _,*, /) : ')
if op=='+':
    print('sum:',a+b)
elif op=='-':
    print('difference:',a-b)
elif op=='*':
    print('product:',a*b)
else:
    print('division',a/b)