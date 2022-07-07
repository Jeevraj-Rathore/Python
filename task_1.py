# Take user input and Display the string it in center, left and right of the line.
# And you also need to find out the total width or columns in a line. To do that so use (mode) in cmd.
# And also get the output in title form

'''
given_str = input("Enter your String: ")
print(given_str.center(181).title())

# To adjust string to extreme left use --> ljust()
print(given_str.ljust(181).title())

# To adjust string to extreme right use --> rjust()
print(given_str.rjust(181).title())
'''

'''
NOTE :-
- Number of columns may differ screen to screen
- So the above code will not work perfectly on all screens
'''

# So use 'os' module instead
# It will automatically identify the total number of columns of your terminal

import os

terminal_width = os.get_terminal_size().columns

given_str = input("Enter your String: ")
print(given_str.center(terminal_width).title())

# To adjust string to extreme left use --> ljust()
print(given_str.ljust(terminal_width).title())

# To adjust string to extreme right use --> rjust()
print(given_str.rjust(terminal_width).title())