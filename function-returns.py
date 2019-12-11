def add(a, b): # function is called with two arguments: a and b
    print(f"ADDING {a} + {b}") # print what the function is doing
    return a + b # add a and b, then return them
    # when the function ends, any line that runs it will be able to assign this a + b result to a variable
    #-- think of this as 'inside out' rather than 'backwards'

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# a puzzle for extra credit
print("Here is the 'what' variable:")

# take the return value of one function and use it as the argument of another function
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("Here is the 'what' variable divided into multiple steps:")
divided = divide(iq, 2)
multiplied = multiply(weight, divided)
subtracted = subtract(height, multiplied)
added = add(age, subtracted)

print(what, "=", added)


