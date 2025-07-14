# * - repeat a character zero or more times
# + - repeat a character one or more times
# ? - matches the expression 0 to 1 times
# ( - indicates where string extraction is to start
# ) - indicates where string extraction is to end

import re
string="From bobby.mark@mail.com"
pattern="ma*"
print(re.findall(pattern, string))

pattern="ma+"
print(re.findall(pattern, string))

pattern="^F.*"
print(re.findall(pattern, string))

pattern="^F.*?"
print(re.findall(pattern, string))

pattern="^F.+?"
print(re.findall(pattern, string))

pattern="From (\S+@\S+)"
print(re.findall(pattern, string))