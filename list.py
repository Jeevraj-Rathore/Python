# List data is the combination of data

my_list1 = [3, 2, 4, "python", 5.6]

# bool(empty_list) ==> False
# bool(non_empty_list) ==> True

print(my_list1[0])
print(my_list1[3])
print(my_list1[-1])
print(my_list1[-2])

print(my_list1[3][1])
print(my_list1[1:])
print(my_list1[1:4])

my_list1[0] = 45
print(my_list1)

my_list = [3,5,2,7,3,8,9]
print(my_list.index(5))
print(my_list.count(10))

'''
print(my_list)
my_list.clear()
print(my_list)
'''

# Ways to copy a list
my_new_list = my_list # No new memory location is created & same address will point to both variables
my_one_list = my_list.copy() # By using copy() another memory location is created for the new variable

print(id(my_list),id(my_new_list))
print(id(my_one_list))

print(my_list)
my_list.append(56) # To add a new data at the last of the list
print(my_list)

my_list.insert(1, 45) # To add data in between of the list
print(my_list)

my_new_list = [5,6]
my_list.extend(my_new_list) # To add a list as an normal data
print(my_list)

# Remove value based on index position
# By default pop() will remove last data if you don't provide the index number
# pop() gives the data that it is going to remove if we use it directly in the print statement
my_list.pop(0)
print(my_list)

print(my_list.pop())
print(my_list)

my_list.reverse()
print(my_list)

# sort() --> It arranges the data in ascending order
my_list.sort()
print(my_list)

'''
NOTE :-
- For descending order 1st do sort() and then reverse()
'''
my_list.sort(reverse=True)
print(my_list)