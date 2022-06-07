# List Methods, lists are mutable and can be modified in place.

# --------------------------------------------------------------------------------------------- #

# Append to an existing list

list1 = []
add_to_list = 1
list1.append(add_to_list)
print(list1)

# --------------------------------------------------------------------------------------------- #

# Indexing, if index not found ValueError will occur

# Example 1 receiving an index
list2 = [1, 2, 3, 4, 5, 6]

print(list2[2])

# Example 2, does something exist in a list. Value Error is raised if not found, use Try/Except to catch error

list_food = ['cheese', 'salami', 'apples', 'banyan']
item = 'cheese'
print(list_food.index(item))

# Alternative
item_index = list_food.index(item)
print(f'Found the Food at Index: {item_index}')

# --------------------------------------------------------------------------------------------- #

# Insert
# Example 1 Replacing item in list with index. Syntax is INDEX then value to replace with.

list2.insert(3, 'the')
print(list2)

# Sort a list from the lowest value to highest. If string is provided it will sort strings in ASCII number
# Sort can only work with list with all same type of data.
# Sort is a modifier an needs to be used alone and not in a print statement.

# Example 1 All Strings
list3 = ['b', 'z', 'a', 'e', 'c']
list3.sort()

print(list3)

# Example 2 All Ints

list4 = [5, 10, 22, 1, 11, 30]

list4.sort()
print(list4)

# --------------------------------------------------------------------------------------------- #

# Reverse

list5 = [1, 2, 3, 4, 5, 6]

list5.reverse()

print(list5)

# Remove, this will remove the FIRST occurrence of the data in the list. ValueError is raised if not found
# use Try/Except to catch item not found error.

# Example 1
list5 = ['this', 'is', 'python', 'is', 'exam', 'prep', 3]

list5.remove('is')
print(list5)

# Example 2 del statement
# Del function allows for an index value to be specified to more specifically remove items from a list.

del list5[3]
print(list5)

# --------------------------------------------------------------------------------------------- #
#                                          FUNCTIONS                                            #
# --------------------------------------------------------------------------------------------- #

# Min and Max functions

list6 = [10, 11, 20, 34, 100, 3]

print('Max number is list is:', max(list6))
print('Min number in list is:', min(list6))

# OR

result_max = max(list6)
result_min = min(list6)
print(f'Max is {result_max} and Min is {result_min}')

# --------------------------------------------------------------------------------------------- #

# Sum function

print('The sum of list is:', sum(list6))

# Count items in a list, this will count the occurrence of the value passed to count

list7 = [1, 1, 2, 34, 4, 5]
new_list = []
print(list7.count(1))

# Example remove duplicate items from a list

for item in list7:
    if item not in new_list:
        new_list.append(item)

print(new_list)