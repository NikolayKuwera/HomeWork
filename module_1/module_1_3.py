# from os import times
#
# name = 'Nikolay'
# print('Name:', name)
# age = 50
# print('Age:', age)
# age = age + 1
# print('New age:', age)
# is_student = True
# print('Is student:', is_student)
#
# home_task = 12
# hour_count = 1.5
# course_name = 'Python'
# time_for_one_task = ( hour_count / home_task)
# print('Курс:', course_name, ', всего задач:', home_task, ', затрачено часов:', hour_count, ', среднее время выполнения :', time_for_one_task, 'часа')
#
# # Индексация строк
# example = 'Топинамбур'
# print(example[0])
# print(example[-1])
# print(example[5:])
# print(example[::-1])
# print(example[1::2])
#
#
# print('привет,', 'я'.upper(), 'строка в нижнем регистре')
from itertools import count


# def kolglas(k):
#     gl = 'уеёыаоэяиюУЕЁЫАОЭЯИЮ'
#     count = 0
#     for c in k:
#         if c in gl:
#             count += 1
#     return count
#
#
# a = input()
# print(kolglas(a))

# def glas(s):
#     ns = ''
#     for c in s:
#         if c in 'уеыаоэяиюёЁУЕЫАОЭЯИЮ':
#             ns = ns + c
#     return ns
#
#
# a = input()
# print(glas(a))
def поздоровайся(имя):
    print("Привет, " + имя + "!")


def сообщение(имя, вопрос):
    поздоровайся(имя)

    print("Скажи, " + вопрос)


сообщение("Nick", "когда летим на Марс?")
