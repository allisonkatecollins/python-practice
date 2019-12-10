# this one is like your scripts with argv; *args must be in parenthesis to work
#--the * in *args tells python to take all arguments to the fx and then put them in args as a list
# first indented line unpacks the arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# function requirements:
# 1. start function definition with 'def'
# 2. after parenthesis, end first line with a colon
# 3. all lines of code in the function indented 4 spaces
# 4. end function by going back to no indentation