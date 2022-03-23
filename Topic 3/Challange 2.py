s = 0
input = int(input('Enter a positive nuber: '))

for n in range(input+1):
    s += 1/2**n
    print(s)