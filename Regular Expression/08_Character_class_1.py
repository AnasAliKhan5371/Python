import re
# ALL DIGITS
string="91234579"
# "a59566"-match not found
# "9123678484579"-match not found
pattern=r"\d{5}"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")

# ANY NON DIGITS
string="python99"
pattern=r"\D"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")

# NAY ALPHA NUMERIC
string="python"
pattern=r"\w"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")