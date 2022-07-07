# 1. Strip

x = " python  " # provided some spaces by mistake
print(x)

# So to remove that unwanted spaces from left and right use (strip())
print(x.strip())

'''
NOTE :-
- strip() only works for starting left and ending right
- Can't be used to remove something from between the string
'''
x = "python"
print(x.strip('p'))

print(x.strip('n'))

print(x.strip('t'))

# If string has same word both at left and right and you want to remove a specific word use lstrip() or rstrip()
# Or use strip() to remove both

x = "python scripting is easy python"

print(x.lstrip('pyhton'))
print(x.strip('pyhton'))
print(x.rstrip('pyhton'))

# We can also use multiple strip() together
x = "pythonyy"
print(x.strip('p').rstrip('y'))


# 2. Split
x = "python is easy"
print(x.split())
print(x.split('is'))

x = "python is easy and it is very popular"
print(x.split('is'))