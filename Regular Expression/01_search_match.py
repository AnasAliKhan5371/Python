import re

string="babc"
pattern="a"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")

if re.search(pattern,string):
    print("match found")
else:
    print("match not found")
