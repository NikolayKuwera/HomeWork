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

# while True:
#     n = int(input())
#     if n < 10:
#         continue
#     if n > 100:
#         break
#     print(n)
# s = 0
# for i in range(1, 1001):
#     s += i
#     print(s)

# import random
#
# x1 = random.randint(0, 5)
# x2 = random.randint(0, 5)
# x3 = random.randint(0, 5)
# x4 = random.randint(0, 5)
# x5 = random.randint(0, 5)
# print(x1, x2, x3, x4, x5)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for elem in numbers:
    Flag = True
    for divisor in range(2, elem):
        # print(
        #     f'Наш элемент : {elem}, Возможный делитель : {divisor}')  # вот тут вопрос : почему наш элемент 3 и возможный делитель 2?
        if elem % divisor == 0:
            not_primes.append(elem)
            Flag = False
            break
    if Flag == True and elem != 1:
        primes.append(elem)
print(primes)
print(not_primes)
