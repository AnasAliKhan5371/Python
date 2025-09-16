import re

string="91234579"
# "59314678"-match not found
# "9314678"-match not found
pattern=r"^91"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")