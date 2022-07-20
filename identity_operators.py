# 2 Type --> is and is not

x = 6
y = 7
z = 'hi'

# Comapring type() of variables
t1 = type(x) is type(y)
print(t1)

t2 = type(x) is type(z)
print(t2)

t2 = type(x) is not type(z)
print(t2)
