# class name:
#     statements and attributes
#     ----------
#
# call class

# 1:
class car:
    pass          # null operator
c1=car()
print(c1)

# 2:
class car:
    color="black"         # null operator
c1=car()
print(c1.color)

# 3:
class car:
    color="black"
    type="SUV"# null operator
c1=car()
print(c1.color.upper(),c1.type)

#  class functions
class counting:
    n=0
    def cnt(self):     #default parameter
        self.n+=1
        print("counted ",self.n)

c=counting()
c.cnt()
c.cnt()