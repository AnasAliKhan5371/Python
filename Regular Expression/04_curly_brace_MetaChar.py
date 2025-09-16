import re

string="abbc"
# abb-match found
# ab-match not found
pattern=r"ab{2}"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")