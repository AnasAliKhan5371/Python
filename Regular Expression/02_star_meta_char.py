import re

string="abbbbbbbbbbbbbc"
pattern="ab*c"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")

