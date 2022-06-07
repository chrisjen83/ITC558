# Dictionary Methods in Python

# Get Method, if a key is not found no exception will be raised.

# Example 1
dict1 = {'Chris': '55-441143', 'Kathryn': '664-3466', 'Sam': '457-2364'}

#                   KEY ,  Default Error Message
value = dict1.get('Chris', 'Not found')
print(value)

# Item Method, This will return all information in the dictionary into list of Tuples.
# Items will create a DICTIONARY VIEW, using a for loop is best

new_list = dict1.items()
print(new_list)

# You can iterate over the list of tuples and pull out the key and values

for key, value in new_list:
    print(key, value)

# Key Method will print all keys in the dictionary in a DICTIONARY VIEW.

dict_view2 = dict1.keys()

# Iterate over the tuple list and see the keys
for keys in dict_view2:
    print(keys)

# Value method, extracts all the dict values and places them into a DICTIONARY VIEW (List)
list1 = []
values = dict1.values()
print(values)

for item in values:
    list1.append(item)

print(list1)

# Pop Method will remove the supplied key and item from the dict.

# Example 1, Pop and item and make the output into a new dic
new_dict = dict1.pop('Chris', 'No entry')
print(new_dict)
print(dict1)

# Example 2, Pop the item with the dict in place. This modifies the original Dict.
dict1.pop('Chris', 'No entry found')
print(dict1)

# Pop Item Method is used to remove the last key from the dict and output as a tuple.

k, v = dict1.popitem()
print(f'Key is: {k} and value is: {v}')
print(dict1)

# Dictionary Comprehension

dict3 = {'Chris': '55-441143', 'Kathryn': '664-3466', 'Sam': '457-2364'}
copy_phonebook = {}

copy_phonebook = {k: v for k, v in dict3.items()}
print(copy_phonebook)

# Example 2

for key, value in dict3.items():
    print(f' Value = {value}')
    print(f'key = {key}')

# Test if something is in a Dictionary

if 'John' in dict3:
    print('Found Chris')
else:
    print("did not find him")

del dict3['Chris']
print(dict3.items())
