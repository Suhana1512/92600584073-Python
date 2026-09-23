#8. Write a program to illustrate variable scope using local global and nonlocal variables.
# Global variable
x = 10

def outer():
    y = 20

    def inner():
        nonlocal y
        y = 30
        print("Nonlocal:", y)

    inner()

def local():
    z = 40
    print("Local:", z)

print("Global:", x)
local()
outer()
