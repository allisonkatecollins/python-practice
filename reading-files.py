# write two files: a script file and a plain text file that I'll read in the script
# use argv or input to ask user what file to open instead of hardcoding the file's name

# use argv to get a filename
from sys import argv

# two files that I must name when running in the terminal
script, filename = argv

# use 'open' command, which takes a parameter and returns a value I can set to my own variable
# open() creates a file object but doesn't return the contents of the file
txt = open(filename)

# print the contents of the file in the terminal
print(f"Here's your file {filename}:")

# call read() function on txt
# give a file a command by using the dot, the name of the command, and parameters
print(txt.read())

# type 'reading-files_sample.txt'
print("Type the filename again:")
file_again = input("> ")

# if the file name is typed correctly, the terminal will again display the contents of the txt file
txt_again = open(file_again)
print(txt_again.read())

# close files when done with them
txt.close()
txt_again.close()

# to run: python3 reading-files.py reading-files_sample.txt

# to run code within the terminal:
# type "python3" and press enter
# txt = open("reading-files_sample.txt")
# print(txt.read())
# type quit() to escape