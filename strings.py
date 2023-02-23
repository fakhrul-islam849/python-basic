# assign multiple string to a variable either """ or ''' with closing
a = """this is my line,
this is my second line"""
print(a)

# get string position
a = "jewel"
print(a[1])

# looping a string

a = 'jewel'

for x in a:
    print(x)

# getting string length
a = 'jewel'
print(len(a))

# check character present in string
txt = 'my name is jewel'
print('jewel' in txt)
print('Fakhrul' not in txt)

# if statement inside or not  string
if 'jewel' in txt:
    print('jewel exit in text')
if 'Fakhrul' not in txt:
    print('Fakhrul not exit in text')

# ========== string slicing ================
txt = 'Md Fakhrul Islam'
print(txt[0:2]) # slice between index last index not included
print(txt[:2]) # slice from start to index
print(txt[3:]) # slice from start to end

# make string upper case and lower case
print(txt.upper())
print(txt.lower())

# other string function
print(txt.strip())  # remove white space
print(txt.replace('Fakhrul', 'Jewel'))  # replace phrase from string
print(txt.split(' '))   # split

# concatenate string
a = 'fakhrul'
b = 'islam'
print(a + b)
print(a + ' ' + b)

#  format string with integer
age = 27
year = 2023
txt = 'This is {}. I am {}'
print(txt.format(year, age))

# escape a character
quot = "In this string \"Special\" used"  # used  \" or ' in the string for quote " or '
print(quot)
backslash = "In this string \\Special\\ used"  # used \\ for \ in the string
print(backslash)
newLine = "In this string \nSpecial\n used"  # used \n for new line in the string
print(newLine)
cr = "In this string \rSpecial\r used"  # used \r for Carriage Return in the string
print(cr)