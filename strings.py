my_name = "Jeevraj"
my_new_name = "Python Developer"
my_info = '''
I started my carrier as an admin and
moved into automation team
'''
print(f"my name is: {my_name}\nmy new name is: {my_new_name}\nmy info is: {my_info}")

my_str = ""
my_new_str = " "
print(f"{bool(my_new_str)}")

my_fav_scripting = "Python Scripting"
print(f"{my_fav_scripting}")
print(my_fav_scripting)

# Slicing of a string
# Indexing (for +ve start with 0 and for -ve start with -1)
print(my_fav_scripting[0])
print(my_fav_scripting[5])
print(my_fav_scripting[-1]) # for last character of given string

# Using range to print multiple caharacters of a string
print(my_fav_scripting[0:6]) # it will print fromm 0 to 5
print(my_fav_scripting [0:]) # prints till last character

str_0_5 = my_fav_scripting[0:6]
print(str_0_5)
print(my_fav_scripting[:6])
print(my_fav_scripting[4:11])

'''
NOTE :
-> Strings are immutable
-> We can't modify a part of a string
-> But we can delete entire string
-> And we can completely assign new string to te same variable
'''
my_fav_scripting = "Python Tutorials"
print(my_fav_scripting)

# Lenght of a string
my_str_len = len(my_fav_scripting)
print(f"Lenght of the given string is: {my_str_len}")
print(f"Lenght of the given string is: {len(my_fav_scripting)}")

'''
if lenght is 16 :
	+ve indexing = 0 to 15
	-ve indexing  = -16 to -1
'''

# Concatenate(add) a string
my_str1 = "Pyhton"
my_str2 = "Scripting"
my_str3 = my_str1 + " " + my_str2 + " Tutorials"
print(my_str3)

