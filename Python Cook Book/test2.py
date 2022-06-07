# Question 1
numbers = []

for number in range(1, 101):
    numbers.append(number)

print(numbers)

# Question 2
names = ['john', 'smith', 'chris', 'kathryn']

for name in names:
    print(name)

# Question 3
scores = [1, 45, 100, 33, 28, 99, 1020, 10]

scores.sort(reverse=True)
max_score = max(scores)
print(scores)
print(f'max number is {max_score}')

# Question 5

def list_sum(list):
    return sum(list)

list1 = [1,2,3,4,5,6, 100, 120]

result = list_sum(list1)
print(result)

value = 0
for number in list1:
    value += number

print(value)

# Question 6


if 'ruby' in names:
    print('Hello Ruby')
else:
    print('Why no Ruby?')

# Question 8

new_list2 = [element * 2 for element in list1]
print(new_list2)

# Question 9

new_list3 = [element for element in list1 if element > 100]
print(new_list3)

# Question 10

new_list4 = [element for element in list1 if element % 2 == 0]
print(new_list4)

# Question 1

output_file = open('things.txt', 'w')

output_file.write('cat\nbanana\nAustralia')

output_file.close()

# Question 2

input_file = open('things.txt', 'r')

contents = input_file.read().split('\n')
print(contents)
input_file.close()

# Question 3

output_file1 = open('number_list.txt', 'w')

for number in range(1, 101):
    output_file1.write(f'{str(number)}\n')

output_file1.close()

# Question 4

read_file = open('number_list.txt', 'r')

for item in read_file:
    print(item.rstrip())
read_file.close()

read_file = open('number_list.txt', 'r')
print('While Method\n\n')
line = read_file.readline()

while line != '':
    line.rstrip()
    number = int(line)
    print(number)
    line = read_file.readline()

read_file.close()

# Question 5
read_file = open('number_list.txt', 'r')

count = 0
line = read_file.readline()

while line != '':
    line.rstrip()
    number = int(line)
    count += number
    line = read_file.readline()

print(f'The total of the file is {count:,}')

read_file.close()

# Question 6

read_file1 = open('number_list.txt', 'a')

read_file1.close()

# Question 7
print('Question 7')
read_file2 = open('students.txt', 'r')
output_file2 = open('new_students.txt', 'w')

line = read_file2.readline()

while line != '':
    line.rstrip('\n')
    name = line.split(',')

    if name[0] != 'John Perz':
        output_file2.write(line + '\n')
    line = read_file2.readline()

read_file2.close()
output_file2.close()

# Question 8

read_file3 = open('students.txt', 'r')
output_file3 = open('update_student.txt', 'w')

line = read_file3.readline()

while line != '':
    line.rstrip()
    score = line.split(',')
    if score[0] == 'Julie Milan':
        score[1] = '100'
        output_file3.write(score[0] + ',' + score[1])
    else:
        output_file3.write(line)

    line = read_file3.readline()


read_file3.close()
output_file3.close()

# Question 10

try:
    x = float('abc123')
    print('The conversion is complete')

except ValueError:
    print('This code cause a value error')
except TypeError:
    print('This code cause a Type Error')
except NameError:
    print('This code cause a Name error')

print('The end')

# Question 1
#
# product = 0
#
# while product < 100:
#     user_input = int(input('Enter a number: '))
#     product = user_input * 10

# Question 2

again = 'yes'

while again == 'yes':
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    print(num1 + num2)
    again = input('Go again?').lower()

