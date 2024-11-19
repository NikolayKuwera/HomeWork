import random

elem = random.randint(3, 20)
password = ''
for x in range(1, elem):
    for y in range(x + 1, elem):
        if elem % (x + y) == 0:
            password += f'{x}{y}'
print(f'{elem} - {password}')
