# To check if it is there in a list on not we use membership operators
# Use in or not in

x = [4,5,6,7]
findout1 = 6 in x
print(findout1)

vaild_java = ['1.6','1.7','1.8','1.9']
host_java = '1.5'

if host_java in vaild_java:
    print("Host deployed of Valid Java version")
else:
    print("Host deployed with invalid Java version")