my_set = {4,5,7,2,7,0}
print(my_set)

'''
NOTE :-
- Set will only show unique data
- Set will show data in ascending order
'''
# Convert list into set
my_list = [4,5,6,7,4,5]
new_set = set(my_list)
print(new_set)

a = {3,4,5,6}
b = {5,6,7,8,9}

# 1. Union
abc = a.union(b)
print(abc)

# 2. intersection
ab = a.intersection(b)
print(ab)
