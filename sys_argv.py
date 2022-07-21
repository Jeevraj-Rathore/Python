# It returns a list of command line arguments passed to a python scripts
# While running a script if you pass some values with it. It is known as command line arguments

import sys

if len(sys.argv) != 3:
    print("Usage:")
    print(f"{sys.argv[0]} <your_req_string> <lower|upper|title>")
    sys.exit()

usr_str = sys.argv[1]
usr_action = sys.argv[2]

if usr_action == "lower":
    print(usr_str.lower())
elif usr_action == "upper":
    print(usr_str.upper())
elif usr_action == "title":
    print(usr_str.title())
else:
    print("Your option is invalid. Please select valid option from this list: lower/upper/title")