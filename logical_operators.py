# Type --> and, or, not

a = 3 > 1
b = 1 in [3,4,5]

test1 = a and b
print(test1)

test2 = 1<2 and 2<3 and 3<4
print(test2)

test3 = 2>1 or 3>4
print(test3)

'''
NOTE :-
- Is want to check many conditions together use all() it is same as 'and'
'''
test4 = all([1<2, 2<3, 3<4, 4<5, 5<6, 6<7])
print(test4)

'''
NOTE :-
- Is want to check many conditions together use any() it is same as 'or'
'''
test5 = any([1<2, 2<3, 3<4, 4<5, 5<6, 6>7])
print(test5)