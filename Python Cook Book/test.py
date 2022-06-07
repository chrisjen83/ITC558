# Question 1
dict1 = {'a': 1, 'b': 2, 'c': 3}

# Question 2
dict2 = {}

# Question 3
dct = {'James': 1, 'Chris': 2, 'Kathryn': 3, 'Jon': 4}
search = 'Chris'

if search in dct.keys():
    print(dct.get(search))
else:
    print(f'{search} was not found in dictionary')

# Question 4
item_search = 'Jon'

if item_search in dct.keys():
    value = dct.get(item_search)
    dct['John'] = value
    del dct[item_search]
else:
    print('there is no item in the dictionary')

print(dct)

# Question 11
numbers = [1, 2, 3, 4, 5]

new_dct = {number: (number * 10) for number in numbers}
print(new_dct)

# Question 12
test_average = {
    'Janelle': 98,
    'Sam': 87,
    'Jennifer': 92,
    'Thomas': 74,
    'Sally': 89,
    'Zeb': 84
}

high_score = {name: score for name, score in test_average.items() if score >= 90}

print(high_score)

# Question 1
choice = 'n'
if choice.upper() == 'Y':
    print('Yes, it is')

# Question 2
count = 0
mystring = 'this is a space counting test'

for space in mystring:
    if space == 't':
        count += 1
print(count)

# Question 3
count_2 = 0

for alpha in mystring:
    if alpha.isalnum():
        count_2 += 1
print(count_2)

# Question 4
count_3 = 0

for char in mystring:
    if char.lower():
        count_3 += 1
print(count_3)

# Question 5

def starts_with(word):
    if word.startswith('https'):
        result = True
    else:
        result = False

    return result

result = starts_with('word.com')
print(result)

# Question 6

string1 = 'This is a sTring i need to copy'
string2 = ''

for char in string1:
    if char == 'T':
        char = char.lower()

    string2 += char

print(string2)

# -------------------------------------------- #

new_string = string1.replace('T', 't')
print(new_string)

# Question 8

def swap(sentance):
    return sentance[::-1]

result = swap('this is a sentance')
print(result)

# Question 9
print(mystring[:3])

# Question 10
levels = 'Beginner, Average, Advanced, Expert'

levels_list2 = levels.split(',')
print(levels_list2)

# Question 1
numbers = [10, 20, 30, 40, 50]

print(len(numbers))

# Question 2
letters = ['A', 'B', 'C', 'D']

print(f'Value at index 1: {letters[1]}')
print(f'Value at index 3: {letters[3]}')
print(f'Value at index -1: {letters[-2]}')

# Question 3

values = [2, 4, 6, 8, 10]

print(values[1:3])

# Question 4

number1 = [5, 4, 3, 2, 1, 0]

print(number1[:3])

# Question 5
number2 = [1,2,3,4,5,6,7,8]
print(number2[-4:])

# Question 6
values1 = [2] * 5
print(values1)