'''
usr_num = eval(input("Enter a number between 1 to 10: "))

if usr_num in [1,2,3,4,5,6,7,8,9,10]:
    if usr_num == 1:
        print("One")
    elif usr_num == 2:
        print("Two")
    elif usr_num == 3:
        print("Three")
    elif usr_num == 4:
        print("Four")
    elif usr_num == 5:
        print("Five")
    elif usr_num == 6:
        print("Six")
    elif usr_num == 7:
        print("Seven")
    elif usr_num == 8:
        print("Eight")
    elif usr_num == 9:
        print("Nine")
    else:
        print("Ten")
else:
    print("Entered wrong number. Please select between 1 - 10")
'''

# Better way use Dictionary
num = eval(input("Enter a number between 1 to 10: "))

num_word = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"}

if num in [1,2,3,4,5,6,7,8,9,10]:
    print(num_word.get(num))
else:
    print("Entered wrong number. Please select between 1 - 10")
