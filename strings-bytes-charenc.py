# strings, bytes, and character encoding (ex 23)
# concepts:
# 1. how computers store languages for display and processing and how python 3 calls this 'strings'
# 2. how I must "encode" and "decode" python's strings into a type called 'bytes'
# 3. how to handle errors in my string and byte handling

# use languages.txt for this, which contains a list of languages encoded in UTF-8

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    # first thing the fx does is read one line from the languages.txt file
    line = language_file.readline()

    # 'if line' tests for an empty string
    # as long as the string isn't empty, the statement is true and the code below it will run
    # once it's false, that code will be skipped
    if line:
        # call a different function to do the printing of the line
        print_line(line, encoding, errors)
        # call the function again inside itself, creating a loop; the if statement prevents it from going on forever
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # strip the trailing \n on the 'line' string
    next_lang = line.strip() 
    # 'next_lang' is a string, so encode it into raw bytes with .encode()
    raw_bytes = next_lang.encode(encoding, errors=errors) 
    # do the inverse of the previous line by decoding the bytes back into a string
    cooked_string = raw_bytes.decode(encoding, errors=errors) 

    # left: the numbers for each byte of the UTF-8 (shown in hexadecimal)
    # right: character output as actual UTF-8
    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

# utf-8, utf-16, and big5 are each called a 'codec' in python, but use the parameter 'encoding'
# a byte is a sequence of 8 bits (1s and 0s)
# ASCII is the most popular standard that maps a number to a letter
# -- ex: 90 is Z, which in bits is 1011010, which gets mapped to the ASCII table inside the computer
# problem: ASCII only encodes English and a few other similar languages
# -- solution: Unicode, which lets you use 32 bits to encode a character (instead of 8)
# convention for encoding text in python is "UTF-8", which means Unicode Transformation Format 8 bits
# -- use 8 bits for most characters and escape into 16 or 32 bits as needed - this prevents wasted space

# in python a 'string' is a UTF-8 encoded sequence of characters for displaying or working with text
# the 'bytes' are then the "raw" sequence of bytes that python uses to store the string
# output will start with b' to tell python you're working with raw bytes

# to run: python3 strings-bytes-charenc.py utf-8 strict