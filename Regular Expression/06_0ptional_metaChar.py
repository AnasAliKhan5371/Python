import re

string="pythonfile"

# "python-file"-match found
pattern=r"python-?file"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")