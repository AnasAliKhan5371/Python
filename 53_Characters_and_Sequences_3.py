# []
# [aeiou] - matches single character in listed list
# [^XYZ] - matches single character
# [a-z 0-9] - set of characters include a range
# {}

import re

string="python"
pattern="[aeiou]"
print(re.findall(pattern, string))

string="python"
pattern="[^xyz]"
print(re.findall(pattern, string))

string="python3.0"
pattern="[a-z 0-9]"
print(re.findall(pattern, string))

string="python9.0"
pattern="[a-z 0-8]"
print(re.findall(pattern, string))

string="Python"
pattern="[A-Z]"
print(re.findall(pattern, string))

string="Pythonnn"
pattern="Python{2}"
print(re.findall(pattern, string))

string="Pythonnn"
pattern="Python{4}"
print(re.findall(pattern, string))

string="Pytthon"
pattern="Pyt{2}hon"
print(re.findall(pattern, string))

string="From bobby.mark@mail.com"
pattern="@([^ ]*)"
print(re.findall(pattern, string))