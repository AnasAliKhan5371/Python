# format()
# 1
name="mike"
n=len(name)
print(n)
print("hello {},your lucky no. is {}.".format(name,n))

# 2
ex='format() method'
string="this is an example of {} on a string.".format(ex)
print(string)

# 3
first='apple'
second='ball'
third='cat'
string="{} {} {}".format(first,second,third)
print(string)
string="{0} {2} {1}".format(first,second,third)
print(string)

# 4
price=150
with_tax=150+50
print("price: Rs{:.2f}. With Tax: {:.2f}".format(price,with_tax))