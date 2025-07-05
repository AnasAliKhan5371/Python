# capitalize()
a='krishantH'
print(a.capitalize())

# upper()
print(a.upper())

# lower()
print(a.lower())

# check if number or alphabet
b='7'
print(b.isnumeric())
print(b.isalpha())

# start & end with
a= 'mike is a good boy.'
print(a.startswith('mike'))
print(a.endswith('bot'))

# replace a word
print(a.replace('mike','nick'))

# check a letter
print(a.find('a'))

a='   mike is a good boy   '
# remove front space
print(a.lstrip())

# remove end space
print(a.rstrip())

# split()
print(a.split())

# splitlines()
print(a.splitlines())

# join()
a='mike','nick'
b=','
print(b.join(a))