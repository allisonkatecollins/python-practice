days = "Mon Tue Wed Thu Fri Sat Sun"
# \n starts each value on a new line; \n is a new line character
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

# 3 quotes lets you type a string across multiple lines; can do double or single quotes
print("""
type 
words
lots of them
""")

"I am 6'2\" tall." # escape double-quote inside string
'I am 6\'2" tall.' # escape single-quote inside string

tabby_cat = "\tI'm tabbed in." # horizontal tab
persian_cat = "I'm split\non a line." # new line
backslash_cat = "I'm \\ a \\ cat." # backslash between words

fat_cat = '''
I'll do a list:
\t*Cat food
\t*Fishies
\t*Catnip\n\t*Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
