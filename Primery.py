# for i in range(1, 11):                                   # Таблица умножения
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
from subprocess import check_output


# dict_1 = {"a": 1, "b": 2, "c": 3}     # Перебор значений словаре
# for i in dict_1:
#     print(i, dict_1[i])
#
# dict_2 = {"a": 1, "b": 2, "c": 3}        # Перебор значений словаре
# for i, k in dict_2.items():
#     print(i, k)

# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
#
# print(summa(5))

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  # найти чила в списке  <5
# for elem in a:
#     if elem < 5:
#         print(elem)
#
# print([elem for elem in a if elem < 5])  # списковое включение

# salary = [2500, 1358, 4231.455, 7520.5, 5500]    # Пример выведения сред. ЗП , вывод по имени
# print(round(sum(salary) / len(salary), 2), 'Средняя зарплата в компании')
# print(min(salary))
# names = ["Kolya", 'Vanya', 'Vova', 'Natasha', 'Gleb']
# zipped = dict(zip(names, salary))
# print(zipped['Vova'])


# Поиск максимального значения
# def find_max(list_):
#     max_ = list_[0]
#     for i in list_:
#         if i > max_:
#             max_ = i
#     return max_
#
#
# print(find_max([1, 5, 0, 256, -1, 15]))

# Подсчет четных чисел
# def count_even(list_):
#     counter = 0
#     for i in list_:
#         if i == 0:
#             continue
#         if i % 2 == 0:
#             counter += 1
#
#     return counter
#
#
# print(count_even([1, 5, 4, 8, 3, 6, 0]))


# def unicum(list_):
#     new_list = []
#     for i in list_:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
#
#
# print(unicum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = f"""
    Hi {name}. 
    You are a {profession}. 
    You were in {affiliation}.
"""

print(message)
