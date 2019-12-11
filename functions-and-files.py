from sys import argv

script, input_file = argv

# f variable is a file
# --a file is like an old tape; it has a "read head" which you can move around the file
# so print_all() prints the contents of the file
def print_all(f):
    print(f.read())

# f.seek(0) moves you to the start of the file (i.e. the 0 byte)
# so rewind() moves the read head to the start of the file
def rewind(f):
    f.seek(0)

# each time you do f.readline() you're reading a line from the file 
# -- and moving the read head to the right after the \n that ends that line
# so print_a_line() moves the next line one space to the right of the line number, 
# -- and skips a line before printing the next one
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "") # end = "" prevents adding double \n to each line, so it doesn't skip a line

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# current_line stands in for line_count here
current_line = 1
print_a_line(current_line, current_file)

# current line = 2
current_line += current_line 
print_a_line(current_line, current_file)

# current line = 3
current_line = current_line + 1
print_a_line(current_line, current_file)