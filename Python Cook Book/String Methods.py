# Strings are immutable and cannot be modified. There is some exceptions to this rule

# --------------------------------------------------------------------------------------------- #
#                                      MODIFYING STRING                                         #
# --------------------------------------------------------------------------------------------- #


mystring = ' Christopher Jenkins\n'
yourstring = 'Python Course'
splitstring = '10/12/2022'

# --------------------------------------------------------------------------------------------- #

# Lower/Upper Case conversion, modifies the string inplace.

# Example 1
print(mystring.lower())
print(mystring.upper())

# Example 2
if mystring.lower() == yourstring.lower():
    print('The strings are the same')
else:
    print('The strings are not the same')

# Example 3
user_input = input('Enter a name: ').lower()
print(user_input)

# --------------------------------------------------------------------------------------------- #

# lstrip, removes leading \n, \t and whitespaces. Modifies inplace

# Example 1

print(mystring.lstrip())

# --------------------------------------------------------------------------------------------- #

# rstrip, removes all trailing \n, \t and whitespace. Modifies inplace
print(mystring.rstrip())

# strip removes all leading and trailing \n, \t and whitespaces. Modifies inplace

print(mystring.strip())

# --------------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------------- #
#           Search and Replace String Methods, NEED TO MAKE COPIES OF STRINGS!!                 #
# --------------------------------------------------------------------------------------------- #

# end/startswith method which finds substrings in strings. Response is True if the substring is present.
if mystring.endswith('\n'):
    print('Found end substring')
else:
    print('Substring not found')

search = mystring.endswith('\n')
print(search)

# --------------------------------------------------------------------------------------------- #

# Find, will find the first occurrence of the substring and return an index. If does not exist return -1

# Example 1
position = mystring.find('ris')
print(f'Index number {position}')
print(mystring[position])

# Example 2 - Use the in keyword. This returns a boolean where find returns the index.
result = 'h' in mystring
print(f'in testing result: {result}')

# --------------------------------------------------------------------------------------------- #

# Replace, returns a new copy of the string with the replaced word. Syntax is existing string, replaced with.
# Items must be strings. Partial matches for strings will work.

newstring = mystring.replace('Jenkins', 'Smith')

print(f'Replaced String {newstring}')
print(f'Old String {mystring}')

# --------------------------------------------------------------------------------------------- #

# String Splitting, this will take a split character like , or \ and return a list of items.

split_result = splitstring.split('/')
print(split_result)

# --------------------------------------------------------------------------------------------- #

# String slicing will take a start and end index which is valid and create a new string.
# [START:END]
# [:5] this will start at index 0 up to but not including index 5
# [5:] this will start at index 5 and continue till the end of the string.

# Example 1
print(mystring[:6])

# Example 2
print(mystring[2:len(mystring)])

# Example 3 Reversing a string
# Use the slice method and use [::-1]

string1 = 'this is a string to reverse'
print(string1[::-1])
