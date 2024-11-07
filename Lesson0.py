
print(1234//10%100+5678//10%100)
print(int(13.42) == int(42.13 * 100) % 100)


animal = 'fish'
print(animal[0].upper() + animal[1:-1] + animal[-1].upper())


first_name = ('Nikolay')
last_name = ('Ovsyannikov')
greeting = ('Зравствуйте, ' + first_name + (' ') + last_name + ('!'))
print(greeting)

a=['dog','cat']
b=['giraff', 'gorilaz']
a.append('cow')
a.extend(b)
d='man'
a.extend(d)
a[2] = 'kakadu'
print(a)

tuple = (1,[2, 3],[4, 5])
print(tuple)
tuple[1][0] = 6

print(tuple)



