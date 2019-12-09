# parameters, unpacking, variables

# an import is how I add modules (i.e., features) to my script from the Python feature set
# argv is the argument variable, which holds the arguments I pass to my python script when I run it
from sys import argv

# here I unpack argv - so I take whatever is in it, unpack it, and assign it to these 4 variables in order
script, first, second, third = argv

# now print them out like normal
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

name = input("whats ur name ")
print(f"hi {name}, you live in {script} now")

# to run on command line:
# python3 unpacking-args.py first 2nd 3rd
# I can replaced 'first, 2nd, 3rd' with any 3 things I want; if not given 3 things, I get an error