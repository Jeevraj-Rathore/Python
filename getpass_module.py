# Used to hide the password entered by the user

import getpass

db_pass = getpass.getpass(prompt="Enter your password: ")
print(f"The entered password is: {db_pass}")