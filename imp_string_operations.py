x = "python"

# 1. join() (use this to add something between the string)
y = "-".join(x)
print(y)

print(x)

print("*".join(x))

print("\n".join(x))

print("\t".join(x))

# 2. center() (use this to print your string in center of the given spaces)
my_str = "Python"
my_str1 = "Python Scripting"
my_str2 = "String Operation"

print(my_str.center(20))

print(f"{my_str.center(20)}\n{my_str1.center(20)}\n{my_str2.center(20)}")

# 3. zfill() (it adds zero's in front of a string) (also called as padding)
print(my_str.zfill(10))
