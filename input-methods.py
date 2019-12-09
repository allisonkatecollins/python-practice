#print("How old are you?", end=' ') # end=' ' tells `print` to not end the line with a newline character & go to the next line
#age = input()
#print("How tall are you?", end=' ')
#height = input()
#print("How much do you weigh?", end=' ')
#weight = input()

# type input directly in terminal to get output here
# whatever you type will be converted into a string unless it's typecast
#print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# putting the question inside the input() yields the same result as above
#the space after the ? separates the question from the answer
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")