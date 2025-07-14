import re
from re import findall

pattern="apple"
if re.match(pattern,"apple"):
    print("true")
else:
    print("false")

# findall(pattern,string,flags)

pattern="apples"
string=re.findall("app",pattern)
print(string)

string=re.findall("XYZ",pattern)
print(string)