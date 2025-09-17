# basic calculator that performs addition, subtraction, multiplication, or division based on user input.
num1=float(input("First number : "))

operator=input("Operation(+, -, *, /) : ")

num2=float(input("Second number : "))

if operator=='+':
    ans=num1+num2
elif operator=='-':
    ans=num1-num2
elif operator=='*':
    ans=num1*num2
elif operator=='/':
    if num2==0:
        print("Error : Division by zero not allowed.")
        exit(0)
    ans=num1/num2
else:
    print("Error : Invalid Operator.")
    exit(0)
print(f"\nResult : {num1} {operator} {num2} = {ans}")
