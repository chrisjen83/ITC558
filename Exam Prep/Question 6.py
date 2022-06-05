# Question 6A

with open('hello.txt', 'w') as hfile:

    hfile.write('treat each other\nwith respect.')

# Question 6B

hfile = open('hello.txt', 'r')

somevar = hfile.read()

# Prints the number of elements after splitting
print(len(somevar.split(' ')))

# Prints the string index of where ea first appears in the file.
print(somevar.find('ea'))

hfile.close()



