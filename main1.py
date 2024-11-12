n = list(range(1, 21))
b = n.copy()
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
else:
    print(n)
    print(m)
print(b)

# from time import sleep
#
# a = 5
# print(a)
# print('я тут')
# sleep(4)
# print('Фух 4 секунды прошло')
