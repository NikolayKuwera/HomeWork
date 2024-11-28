# n = int(input('Введите число: '))
# old = n % 10
# n = n // 10
# f = 0
# while n != 0:
#     p = n % 10
#     if p == old:
#         f = 1
#         n = n // 10
#         old = p
#     if f == 1:
#         print('Да')
# else:
#     print('нет')


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
#     n = int(input('Введите число 0 , что бы закончить цикл'))
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

# x = int(input())  # Поиск кол-ва цифр, четных цифр, сумма , произведение цифр , мин и макс число
# kol = 0
# kol_ch = 0
# s = 0
# pr = 1
# max = 0
# min = 9
# while x > 0:
#     last = x % 10
#     kol = kol + 1
#     if last % 2 == 0:
#         kol_ch += 1
#     s = s + last
#     pr = pr * last
#     if last > max:
#         max = last
#     if last < min:
#         min = last
#     x = x // 10
# print("Всего цифр", kol)
# print("Всего четных цифр", kol_ch)
# print("Сумма всех цифр", s)
# print("Произведение цифр", pr)
# print("Maximum", max)
# print("Minimum", min)

# first_name = input('Как вас зовут? in lowercase:')
# second_name = input('Как ваша фамилия? in lowercase:')
# first_name = first_name.title()
# second_name = second_name.title()
# name = first_name + ' ' + second_name
# print(name)

# stroka = input("Напишите строку: ")
# print(len(stroka))
# start = int(input('Введите число начало строки '))
# end = int(input('Введите последнее число строки'))
# text = (stroka[start:end])
# print(text)

# first_name = input('Как вас зовут ? :')
# if len(first_name) < 5:
#     second_name = input('Как ваша фамилия ? :')
#     Name = first_name + second_name
#     print(Name.lower())
#
# else:
#     print(first_name.upper())

# word = input('введите слово: ')
# first = word[0]
# lenght = len(word)
# rest = word[1:lenght]
# if first != 'а' and first != 'у' and first != 'е' and first != 'о' and first != 'и':
#     newword = rest + first + 'ай'
# else:
#     newword = word + 'вай'
# print(newword.lower())

# import math    # вычисление квадратного корня
#
# number = int(input('Введите число больше "500'))
# answer = math.sqrt(number)
# print(round(answer, 2))

# a = int(input())
# b = int(input())
# ans_1 = a // b
# ans_2 = a % b
# print('Если ', a, 'разделить на ', b, 'то получится', ans_1, 'с остатком', ans_2)

# print("1) Square")  # выбор расчета площади или периметра
# print("2) Triangle")
# print()
# menuselection = int(input("Enter a number: "))
# if menuselection == 1:
#     side = int(input("Enter the length of one side: "))
#     area = side * side
#     print("The area of your chosen shape is ", area)
# elif menuselection == 2:
#     base = int(input("Enter the length of the base: "))
#     height = int(input("Enter the height of the triangle: "))
#     area = (base * height) / 2
#     print("The area of your chosen shape is ", area)
# else:
#     print("Incorrect option selected")

# name = input("Type in your name: ")  # Ввести имя и кол-во раз.вывести каждую букву = цифре
# num = int(input('Введите число: '))
# for x in range(0, num):
#     for i in name:
#         print(i)


# num = int(input('Введите число от 1 до 12 :')) # таблица умножения
# for i in range(1, 13):
#     x = i * num
#     print(i, 'x', num, '=', x)

# num = int(input('Введите число до 50 :')) #обратный отсчет до выбранного числа включительно
# for x in range(50, num - 1, -1):
#     print(x)

# name = input('Введите ваше имя : ') # Повторить имя  N раз и если больше 10 , то вывести 3 раза "Too high"
# num = int(input('Введите число: '))
# if num < 10:
#     for i in range(0, num):
#         print(name)
# else:
#     for i in range(0, 3):
#         print('Too high')


# total = 0     # Ввести число от 0 до 5 ,спросить добавить число в перемен. Total .вывести Тотал
# for i in range(0, 5):
#     num = int(input('Введите число'))
#     ans = input('Добавить число в ответ?, (y / n) ')
#     if ans == 'y':
#         total = total + num
# print(total)


# direction = input('В каком порядке вводить число : UP /DOUN ? (u/d)')
# if direction == 'u':
#     num = int(input('Введите число :'))
#     for i in range(1, num + 1):
#         print(i)
# elif direction == 'd':
#     num = int(input('Введите число < 20 :'))
#     for i in range(20, num - 1, -1):
#         print(i)
# else:
#     print('I don’t understand')

# number = int(input('Сколько людей хочешь пригласить на вечеринку ? :'))
# if number < 10:
#     for i in range(1, number):
#         name = input('Назови имя :')
#         print(name, 'has been invited')
# if number >= 10:                              # Можно так же заменить на else
#     print('Too many people')

# num = 0
# while num <= 5:
#     num = int(input("Enter a number: "))
# print("The last number you entered was a", num)


# num_1 = int(input('Введите  число : '))  #предлагаем ввести число, если ответ yes , то добавляем число в Total
# total = num_1
# again = 'y'
# while again == 'y':
#     num_2 = int(input('Введите еще число : '))
#     total = total + num_2
#     again = input('Ввести еще число ? : y / n ')
# print('total is :', (total))


# guest = 0  # Приглашаем людей на вечеринку
# again = 'y'
# while again == 'y':
#     name = input('Кого вы хотите пригласить ? :')
#     print(name, 'has been invited')
#     again = input('Кто то еще придет ? :  y / n ')
#     guest = guest + 1
# print('На вечеринку прийдет :', guest)


# compnum = 50  # Отгадываем число
# num = int(input('Введите число : '))
# count = 1
# while num != compnum:
#     if num < compnum:
#         print('To low')
#     else:
#         print('To hight')
#     count = count + 1
#     num = int(input('Введите число : '))
# print('Отлично! Вы угадали! вы использовали : ', count, 'попыток')

# num = int(input('Введите число от 10 до 20 : '))  # Еще отгадываем число
# while num < 10 or num > 20:
#     if num < 10:
#         print('To low , попробуй еще')
#     else:
#         print('To hight , попробуй еще')
#     num = int(input('Попробуй еще : '))
# print("Спасибо!")

# num = 10    # Игра перебираем бутылки
# while num > 0:
#     print('На стене висело', num, 'зеленых бутылок')
#     print(num, 'зеленых бутылок висело на стене')
#     print('И если 1 зеленая бутылка упала, то сколько осталось на стене ?')
#     num = num - 1
#     answer = int(input('Сколько зеленых бутылок будет висеть на стене ?'))
#     if answer == num:
#         print('На стене будет висеть', num, 'бутылок')
#     else:
#         while answer != num:
#             answer = int(input('Попробуй еще : '))
# print('На стене больше нет зеленых бутылок')

# import random   # Орел или Решка
#
# coin = random.choice(['h', 't'])
# guess = input('Выбери (t)ails or (h)eds :')
# if guess == coin:
#     print('Ты угадал!')
# else:
#     print('Удача не на твоей стороне!')
# if coin == 'h':
#     print('Выпало : heads')
# else:
#     print('Выпало : tails')

# import random  # Угадываем число от 1 до 5
#
# num = random.randint(1, 5)
# guess = int(input('Выберите число от 1 до 5'))
# if guess == num:
#     print('Well don')
# elif guess > num:
#     print('To hight , Попробуй еще')
#     guess = int(input('Выберите число от 1 до 5'))
#     if guess == num:
#         print("Correct")
#     else:
#         print('You loss')
# elif guess < num:
#     print('To low , Попробуй еще')
#     guess = int(input('Выберите число от 1 до 5'))
#     if guess == num:
#         print("Correct")
#     else:
#         print('You loss')

# import random  # Продолжаем угадывать числа
#
# num = random.randint(1, 10)
# correct = False
# while correct == False:
#     guess = int(input('Выбери число :'))
#     if guess == num:
#         correct = True
#     elif guess < num:
#         print('To low')
#     else:
#         print('To hight')
# print('Угадал')


# import random  # Угадываем ответы на сложение
#
# score = 0
# for i in range(1, 6):
#     num1 = random.randint(1, 50)
#     num2 = random.randint(1, 50)
#     correct = num1 + num2
#     print(num1, "+", num2, "= ")
#     answer = int(input("Your answer: "))
#     print()
#     if answer == correct:
#         score += 1
# print("You scored ", score, " out of 5")

# import random  # Угадываем цвет
#
# colour = random.choice(['red', 'blue', 'green', 'pink', 'white'])
# print('Выбери цвет из : red, blue, green, pink, white')
# tryagain = True
# while tryagain == True:
#     theirchoice = input("Ваш цвет: ")
#     theirchoice = theirchoice.lower()
#     if colour == theirchoice:
#         print("Well done")
#         tryagain = False
#     else:
#         if colour == "red":
#             print("Ты покраснел")
#         elif colour == "blue":
#             print("Какое небо голубое.")
#         elif colour == "green":
#             print("прям позеленел от злости.")
#         elif colour == "white":
#             print("белеет мой парус такой одинокий..?")
#         elif colour == "pink":
#             print("все девочки любят этот цвет")

# import turtle   # квадрат
#
# for i in range(0, 4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.exitonclick()

# import turtle  # Рисуем треугольник
#
# for i in range(0, 3):
#     turtle.forward(150)
#     turtle.right(120)
# turtle.exitonclick()

# import turtle  # Рисуем круг
#
# for i in range(0, 360):
#     turtle.forward(1)
#     turtle.right(1)
# turtle.exitonclick()

# import turtle   # Рисуем 3 квадрата, заполняем их цветом
#
# turtle.color("black", "red")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
#
# turtle.pendown()
# turtle.color("black", "yellow")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
#
# turtle.pendown()
# turtle.color("black", "green")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.end_fill()
# turtle.exitonclick()

# import turtle  # Рисуем пятиконечную звезду
#
# for i in range(0, 5):
#     turtle.forward(100)
#     turtle.right(145)
# turtle.exitonclick()

# import turtle
#
# turtle.left(90)  # Рисуем единицу
# turtle.forward(100)
# turtle.right(90)
# turtle.penup()
#
# turtle.forward(50)  # Рисуем двойку
# turtle.pendown()
# turtle.forward(75)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(75)
# turtle.penup()
#
# turtle.forward(50)  # Рисуем тройку
# turtle.pendown()
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(45)
# turtle.left(180)
# turtle.forward(45)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(75)
#
# turtle.hideturtle()
# turtle.exitonclick()

# import turtle   # Рисуем восьмиугольник с разными по цвету сторонами
# import random
#
# turtle.pensize(3)
# for i in range(0, 8):
#     turtle.color(random.choice(["red", "blue", "yellow", "green", "pink", "orange"]))
#     turtle.forward(50)
#     turtle.right(45)
# turtle.exitonclick()

# import turtle    # Рисуем рисунок
#
# for x in range(0, 10):
#     for i in range(0, 8):
#         turtle.forward(50)
#         turtle.right(45)
#     turtle.right(36)
#     turtle.hideturtle()
# turtle.exitonclick()


# import turtle   # Случайный рисунок
# import random
#
# lines = random.randint(5, 20)  # выбираем кол-во линий
# for x in range(0, lines):
#     length = random.randint(25, 100)   # выбираем длину линии
#     rotate = random.randint(1, 365)    #  выбираем угол
#     turtle.forward(length)
#     turtle.right(rotate)
# turtle.exitonclick()

# names_list = ["John", "Tim", "Sam"]  # Добавление в список и сортировка в алфавите
# names_list.append(input("Add a name: "))
# names_list.sort()
# print(names_list)

# colours = {1: "red", 2: "blue", 3: "green"}   # замена в словаре по индексу
# colours[2] = "yellow"
# print(colours)

# x = [154, 634, 892, 345, 341, 43]   # Ищем введенное число в списке
# num = int(input("Enter number: "))
# if num in x:
#     print(num, " is in the list")
# else:
#     print("Not in the list")

# x = [154, 634, 892, 345, 341, 43]  # Добавление и удаление из списка
# x.insert(2, 420)
# x.remove(341)
# x.append(1974)
# print(x)

# country_tuple = ("Russia", "USA", "Canada", "China", "Egipt")  # Поиск индекса кортеже по названию
# print(country_tuple)
# country = input("Назовите страну из списка : ")
# print("Индекс", country, country_tuple.index(country))

# country_tuple = ("Russia", "USA", "Canada", "China", "Egipt")  # Поиск в кортеже по индексу
# print(country_tuple)
# country = input("Назовите страну из списка : ")
# num = int(input("Назовите страну из списка от 0 до 4: "))
# print(country_tuple[num])

# sports = ["tennis", "footbol"]
# print(sports)
# sports.append(input("Ваш любимый вид спорта? : "))
# # print(sorted(sports))    # один вариант
# sports.sort()  # Это второй вариант сортировки
# print(sports)  # Это второй вариант сортировки

# удалить объект из списка по выбору
# sch_sub = ["Математика", "Русский язык", "Литература", "Биология", "Химия", "Физкультура"]
# print(sch_sub)
# dislike = input("Какой предмет вам не нравится? :")
# sch_sub.remove(dislike)
# print(sch_sub)

# menu = {}
# menu_1 = input("Какое блюдо вам нравится? :")
# menu[1] = menu_1
# menu_2 = input("Какое еще блюдо вам нравится? :")
# menu[2] = menu_2
# menu_3 = input("Какое блюдо вам нравится? :")
# menu[3] = menu_3
# menu_4 = input("Какое блюдо вам нравится? :")
# menu[4] = menu_4
# print(menu)
# menu_del = int(input("Какое блюдо вам не нравится? : "))
# # menu.pop(menu_del)    # один вариант удаления из словаря
# del menu[menu_del]
# print(sorted(menu.values()))


#                         # Делаю срез по списку, указываем начало и конец среза
# colours = ["red", "blue", "green", "black", "white", "pink",
#            "grey", "purple", "yellow", "brown"]
# start = int(input("Введите числа в диапазоне от (0-4) :"))
# end = int(input("Введите последние числа от (5-9) :"))
# print(colours[start: end])  # Срез делает в квадратных скобках !!


# spisok = [345, 678, 987, 321]    # называем число, ищем в списке, выводим индекс
# for i in spisok:
#     print(i)
# num = int(input("Введите 3х значное число :"))
# if num in spisok:
#     print(num, "позиция в списке : ", spisok.index(num))
# else:
#     print("That is not in the list")

# name1 = input("Enter a name of somebody you want to invite to your party: ")  # продолжаем приглашать на вечеринку
# name2 = input("Enter another name: ")
# name3 = input("Enter a third name: ")
# party = [name1, name2, name3]
# another = input("Do you want to invite another (y/n): ")
# while another == "y":
#     newname = party.append(input("Enter another name: "))
#     another = input("Do you want to invite another (y/n): ")
# print("You have ", len(party), " people coming to your party")
# print(party)
# name = input("Назовите имя гостя : ")
# if name in party:
#     print(name, "позиция в списке :", party.index(name))
# answer = input("Хотите, что бы этот человек присутствовал на вечеринке?"
#                " (y/n) : ")
# if answer == "n":
#     party.remove(name)
#     print(name, " удален из списка ")
# print(party)

# def терминатор(слова):                # ПРИНЦИПЫ функции
#     return "{}".format(слова)
#
#
# сообщение = терминатор("Я еще вернусь...")
# print(сообщение)
#
#
# def поздоровайся(name):                    # ПРИНЦИПЫ функции
#     print("Привет, " + name + "!")
#
#
# def сообщение(name, вопрос):
#     поздоровайся(name)
#     print("Скажи, " + вопрос)
#
#
# сообщение("Илон", "когда летим на Марс?")

# def get_name():                # ПРИНЦИП работы функции
#     user_name = input("Enter your name: ")
#     return user_name
#
#
# def print_Msg(user_name):
#     print("Hello, ", user_name, "!")
#
#
# def main():
#     user_name = get_name()
#     print_Msg(user_name)
#
#
# main()


# def get_data():                             # ПРОДОЛЖАЕМ изучать ФУНКЦИЮ def
#     user_name = input("Enter your name: ")
#     user_age = int(input("Enter your age: "))
#     data_tuple = (user_name, user_age)
#     return data_tuple
#
#
# def message(user_name, user_age):
#     if user_age <= 10:
#         print("Hi ", user_name)
#     else:
#         print("Hello ", user_name)
#
#
# def main():
#     user_name, user_age = get_data()
#     message(user_name, user_age)
#
#
# main()

# def number():
#     num = int(input("Ведите число : "))
#     return num
#
#
# def count(num):
#     n = 1
#     while n <= num:
#         print(n)
#         n += 1
#
#
# def main():
#     num = number()
#     count(num)
#
#
# main()

# def func():
#     a[1] = 85
#     return a
#
#
# a = [1, 2, 3]
# print(a)
#
# print(func())
# print(a)

# class House():  # Классы и объекты на примере строительства домов
#     """Описание дома"""
#
#     def __init__(self, street, number):
#         """Свойство дома"""
#
#         self.street = street
#         self.number = number
#         self.age = 0
#
#     def bild(self):
#         """Строит дом"""
#         print("Дом на улице " + self.street + "под номером " + str(self.number) + " построен")
#
#     def age_of_house(self, year):
#         """Возраст дома"""
#         self.age += year
#
#
# House1 = House("Московская", 20)
# House2 = House("Московская", 21)
# House1.age_of_house(5)
# print(House1.number)
# print(House1.age)
# House2.bild()
#
#
# class ProspectHouse(House):
#     """Дома на проспекте"""
#
#     def __init__(self, prospect, number):
#         super().__init__(self, number)
#         self.prospect = prospect
#
#
# PrHouse = ProspectHouse("Ленина", 5)
# print(PrHouse.prospect)


# s = []
# for i in range(1, 21):
#     if i % 3 == 0:
#         s.append(i)
# print(s)
#
# s1 = [i ** 3 for i in range(1, 21) if i % 3 == 0]
# print(sum(s1))
#
# print(sum([i ** 3 for i in range(1, 21) if i % 3 == 0]))  # Сумма кубов в одну строку
#
# s = []
# for i in range(1, 21):
#     for j in range(1, 51):
#         s.append((i, j))
# print(s)
# s1 = [(i, j) for i in range(1, 21) for j in range(1, 51)]
# print(s1)

# s = []  # Возведение в квадрат полож. числа и куб отриц. числа из списка
# for i in range(-10, 11):
#     if i > 0:
#         s.append(i ** 2)
#     else:
#         s.append(i ** 3)
# print(s)
# s1 = [i ** 2 if i > 0  # короткий способ используя генератор списков
#       else i ** 3
#       for i in range(-10, 11)
#       if i % 2 == 0]
# print(s1)

s = [7, 8, 8, -10, -10]  # генератор множества
set_set = {i for i in s}
print(set_set)

dictionary = {i: i ** 10 for i in s}  # генератор словаря
print(dictionary)
