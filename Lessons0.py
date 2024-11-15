# n = int(input('Введите число: '))
# old = n % 10
# n = n // 10
# f = 0
# while n != 0:
#     p = n % 10
#     if p == old:
#         f = 1
#     n = n // 10
#     old = p
# if f == 1:
#     print('Да')
# else:
#     print('нет')
from os.path import split

# sum = 0
# x = int(input())
# while x != 0:
#     sum += x
#     x = int(input())
# print('Сумма ', sum)

# k = 0
# n = int(input('Введите число'))
# while n != 0:
#     if n % 3 == 0:
#         k += 1
#     n = int(input('Введите число'))
# print(k)

# n = int(input())
# while n % 2 != 0:
#     n = int(input())
# max = n
# while n != 0:
#     if n > max and n % 2 == 0:
#         max = n
#     n = int(input())
# print(max)

# i = 0
# while i < 5:
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     if (a == 0) and (b == 0):
#         break
#     if (a == 0) or (b == 0):
#         continue
#     print(a * b)
#     i += 1

while True:
    n = int(input())
    if n < 10:
        continue
    if n > 100:
        break
    print(n)
