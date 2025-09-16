import re

string="abbc"
# acab-match not found
# ab-match not found
pattern=r"a.b"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")