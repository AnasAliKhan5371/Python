import re

string="ac"
# abc-match found
# abbc-match found
pattern="ab+c"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")