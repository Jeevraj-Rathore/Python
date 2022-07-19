my_empty = ()
my_tuple = (3,4,5)
print(my_tuple)

# Convert empty tuple in boolean = False
# Convert non-empty tuple in boolean = True

my_tuple = (3,4,[5,6,7],8,9) # We can add list to a tuple
print(my_tuple)
print(my_tuple[0])
print(my_tuple[2][1])

'''
NOTE :-
- Once you defined a tuple values can't be changed in that
- Modifying the part of tuple is not possible
- But we can modify the entire tuple
- Tuple has only 2 operations --> Count and Index
'''
# Another way to define tuple
x = 5,8,9
print(x,type(x))
