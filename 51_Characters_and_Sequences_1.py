# ^ - matches beginning of a line
# $ - matches end of a line
# . - matches any character
# \d - matches any digit
# \D -matches any non-digit
# \s - matches white space
# \S - matches ant non-white space

import re
string="It is a 56 dog"
pattern="^"
print(re.findall(pattern,string,flags=0))

pattern="^I"
print(re.findall(pattern,string,flags=0))

# $
print("\n")
pattern="$"
print(re.findall(pattern,string,flags=0))

pattern="g$"
print(re.findall(pattern,string,flags=0))

pattern="$g"
print(re.findall(pattern,string,flags=0))

# .
print("\n")
pattern="."
print(re.findall(pattern,string,flags=0))

pattern="^I."
print(re.findall(pattern,string,flags=0))

pattern="^I..."
print(re.findall(pattern,string,flags=0))

#/d ,/D
print("\n")
pattern="\d"
print(re.findall(pattern,string,flags=0))

pattern="\D"
print(re.findall(pattern,string,flags=0))

#/s ,/S
print("\n")
pattern="\s"
print(re.findall(pattern,string,flags=0))

pattern="\S"
print(re.findall(pattern,string,flags=0))
