import os
'''
terminal_width = os.get_terminal_size().columns

given_str = input("Enter your String: ")
print(given_str)

usr_cnf = input("Do you want to allign text: yes or no ? ")
if usr_cnf == "yes":
    print(given_str.center(terminal_width).title())
    print(given_str.ljust(terminal_width).title())
    print(given_str.rjust(terminal_width).title())
'''
'''
usr_str = input("Enter your string: ")
usr_cnf = input("Do you want to convert your string into lower case? say yes or no: ")
if usr_cnf == "yes":
    print(usr_str.lower())
'''
my_even_no = [0,2,4,6,8,10]
usr_num = eval(input("Enter your number: "))

if usr_num in my_even_no:
    print("Your given number is my even number")