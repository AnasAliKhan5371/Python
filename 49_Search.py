#search(pattern,string,flags)
import re
pattern="apple"
if re.search(pattern,"ballapple",flags=0):
    print("true")
else:
    print("false")

#match()
pattern="apple"
if re.match(pattern,"ballapple",flags=0):
    print("true")
else:
    print("false")