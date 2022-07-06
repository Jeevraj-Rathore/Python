'''
# Simple addition calculator
a = 4
b = 8
result = a+b
print(f"The addition of {a} and {b} is: {result}")

# Taking user input
a = input("Enter a value: ")
b = input("Enter b value: ")
result = a+b
print(f"The addition of {a} and {b} is: {result}")
'''
'''
# By default input takes string data type
# So we can specify the data type with input
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
result = a+b
print(f"The addition of {a} and {b} is: {result}")
'''
# or use "eval" function. It automatically converts given data into particular data type
# when using "eval" always provide string in cotation("")
a = eval(input("Enter a value: "))
b = eval(input("Enter b value: "))
result = a+b
print(f"The addition of {a} and {b} is: {result}")
print(f"type of a: {type(a)} type of b: {type(b)}")
