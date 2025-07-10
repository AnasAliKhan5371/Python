# 1:
'''
class const_dest:
    x=0
    def __init__(self):
        print("Constructed")
    def __del__(self):
        print("Destructed")

cd=const_dest()
'''

# 2:
class car:
    x=0
    def __init__(self,color,type):
        self.color=color
        self.type=type
        print("Constructed")
    def __del__(self):
        print("Destructed")
c=car("black","SUV")
print(c.color)
print(c.type)
c1=car("red","SEDAN")
print(c1.color)
print(c1.type)
