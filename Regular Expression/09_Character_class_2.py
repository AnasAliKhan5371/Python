import re

#1:
string="python"
# "python"-match found
pattern=r"[Pp]ython"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")

#2:
string="cython"
# "bpython"-match found
# "Bpython"-match not found
pattern=r"[a-z]ython"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")

#3:
string="Cython"
# "Bpython"-match found
# "bpython"-match not found
pattern=r"[A-Z]ython"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")

#4:
string="Cython"
# "Bpython"-match found
# "bpython"-match found
pattern=r"[a-zA-Z]ython"

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")

#5:
string="Pyhon"
# "Bpython"-match found
# "bpython"-match not found
pattern=r"[a-z]" #

if re.match(pattern,string):
    print("match found")
else:
    print("match not found")
