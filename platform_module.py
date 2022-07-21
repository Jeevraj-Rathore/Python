import platform

print(f"This is {platform.system()} OS")
print(f"Python version is: {platform.python_version()}")
print(platform.machine())
print(platform.release())
print(platform.platform())
print(platform.architecture())
print(platform.processor())
print(platform.node())
print(platform.uname())