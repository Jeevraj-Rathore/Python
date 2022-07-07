x = "python is easy and it is popular language"

# 1. count()
print(x.count('is'))
print(x.count('p'))
print(x.count('t'))
print(x.count(' '))
print(x.count('easy'))

# 2. index()
print(x.index('p'))
print(x.index('p', 1))
print(x.index('p', 26))

# 3. find() (its similar to index but its better)
print(x.find('p'))
print(x.find('p', 2))
print(x.find('p', 26))
print(x.find('p', 28)) # after 26th their is no 'p' but it will not give error instead it will show -1 as output
