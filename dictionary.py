my_dict = {}
print(my_dict,type(my_dict))
print(bool(my_dict))

my_dict = {'fruit': 'apple', 'animal': 'fox', 1: 'one', 'two': 2} # Key and value pairs
print(my_dict)

print(my_dict['fruit'])
print(my_dict.get('animal'))
print(my_dict.get('three')) # Key 'three' not available but don't show any error but will show 'None' as output

# 1. Clear
'''
my_dict.clear()
print(my_dict)
'''
# 2. Add new pair
my_dict['three'] = 3
print(my_dict)
# NOTE --> If key is already there it will update the value

# 3. For keys only
print(my_dict.keys())

# 4. For Values only
print(my_dict.values())

# 5. Item
print(my_dict.items())

# 6. Copy
y = my_dict.copy()
print(y)

# 7. Update
my_new_dict = {'four': 4}
my_dict.update(my_new_dict) # To add one dictionary to another
print(my_dict)

# 8. Pop (to remove based on key)
my_dict.pop('four')
print(my_dict)

# 9. Popitem (Randomly removes the key value pair)
my_dict.popitem()
print(my_dict)

# 10. fromkeys
keys = ['a','e','i','o','u']
new_dict = dict.fromkeys(keys)
print(new_dict)

# 11. setdefault (if key is already their it will not change if not it will assign new key with given value)
my_dict = {}
my_dict.setdefault('k', 45)
print(my_dict)

my_dict = {'fruit': 'apple'}
my_dict.setdefault('fruit', 'orange')
print(my_dict)
