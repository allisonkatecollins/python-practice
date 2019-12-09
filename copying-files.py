from sys import argv
# exists returns True if a file exists, False if not
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

# len() gets the length of the string that I pass to it, then returns that as a number
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

# to run...
# first make a sample file
# echo "This is a test file." > test1.txt
# then look at it using the 'cat' command - easy way to print file to screen
# cat test1.txt
# now run my script on it
# python3 copying-files.py test1.txt new_file.txt

# result should be new_file.txt contains the text from test1.txt