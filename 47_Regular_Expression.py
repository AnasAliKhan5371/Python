#match(pattern,string,flags)
import re
pattern="apple"
if re.match(pattern,"apple"):
    print("true")
else:
    print("false")

if re.match(pattern,"appleapple"):
    print("true")
else:
    print("false")

if re.match(pattern,"appleappleball"):
    print("true")
else:
    print("false")

if re.match(pattern,"appappleball"):
    print("true")
else:
    print("false")