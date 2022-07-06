'''
Basic data types:
1. Numbers(int, float and complex)
2. Strings
3. Boolean
'''
'''
x = 3
y = 5.5
z = 3 + 4j
print(x, type(x))
print(y, type(y))
print(z, type(z))
# print(x,y,z)

lan_name = "Python Scripting"
print(lan_name)

my_name = 'Jeevraj'
print(my_name, type(my_name))

my_name = "X"
print(my_name, type(my_name))

my_value = True
my_new_value = False
print(my_value, type(my_value))
print(my_new_value, type(my_new_value))
'''

# Typecasting (converting one data type to another)
x = 56
print(x, type(x))
y = str(x)
print(y, type(y))
z = bool(x)
print(z, type(z))
p = 0
print(p, type(p))
q = bool(p)
print(q, type(q))

'''
NOTE:
- Any data type can be converted into boolean
  bool(empty) = False --> bool(None), [], (), {}, "", 0
  bool(non-empty) = True
- Any data type can be converted into a string
- But string can't be converted to all data types
'''

# x = "2.1.3.5" # This string can't be convereted into integer
# print(type(x))
# int(x)

x = "45"
print(type(x))
y = int(x)
print(y, type(y))
