import os

path = "C:\\Users\\jeevr\\Desktop\\test.py"

# print(os.path.sep)
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join(path1, path2))
print(os.path.split(path)) # --> is used to split the path name into a pair head and tail.
print(os.path.getsize(path)) # --> in bytes
print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
print(os.path.islink(path)) # --> to check if it is a soft link or not (true or false)