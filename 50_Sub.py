#sub(pattern repl,string,count,flags)
import re
string="It is a dog"
pattern="dog"
print(re.sub(pattern,"cat",string,count=0,flags=0))