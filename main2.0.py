# print('Введите длины сторон ')
# a, b = map(int, input().split())
# print('Периметр : ', (a + b) * 2)
# print('Площадь : ', a * b)

# n = int(input('Введите номер урока : '))
# start = 8 * 60 + 30
# urok = n * 45
# per = (n - 1) * 10
# tm = start + urok + per
# print(tm // 60, 'ч', ':', tm % 60, 'мин', sep=(''))

a = int(input('Введите число :'))
b = int(input('Введите число :'))
M = a
if b > M:
    M = b
print(M)
