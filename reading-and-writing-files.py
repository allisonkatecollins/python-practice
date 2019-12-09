# there are lots of commands I can give to a file

# close: closes the file; like file -> save
# read: reads the contents of the file. I can assign the result to a variable
# readline: reads just one line of a text file
# truncate: empties the file
# write('stuff'): writes 'stuff' to the file
# seek(0): moves the read/write location to the beginning of the file

from sys import argv

# filename will be designated in the terminal when initially running this script
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# 'w' as a parameter means "open this file in 'write' mode"; without it I get an error "file not open for writing"
#--there is also 'r' for 'read,' 'a' for 'append'
#--can add modifiers to these, such as 'w+', 'r+', 'a+', which will open the file in both read and write mode
#--the default for open() is 'r'(read)
target = open(filename, 'w')

# opening in 'w' mode will overwrite the file, so truncate is redundant here
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1} \n {line2} \n {line3}")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it.")
target.close()

# to run: python3 reading-and-writing-files.py test.txt
# if successful, I'll see a new txt file in the solution explorer in VS code