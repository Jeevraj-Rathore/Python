a = eval(input("Enter your first number: "))
b = eval(input("Enter your secomd number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")