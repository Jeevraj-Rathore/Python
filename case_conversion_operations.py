my_string = "Python Scripting tutorials"
print(my_string)

my_string_lower = my_string.lower()
print(my_string_lower)

print(my_string.upper())

# To check available operations on a variable that contains a string use (dir)
x = "hi"
print(dir(x))

print(my_string.swapcase())
print(my_string.title())

my_new_str = "python scripting"
print(my_new_str.capitalize())

# Instead of lower() we can also use casefold()
print(my_string.casefold())
