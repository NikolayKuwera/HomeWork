from pickle import FLOAT

my_dict = {"Nikolay" : 1974, "Gleb" : 2011, "Vladimir" : 2018, "Sasha" : 2020}
print('Dict:', my_dict)
print('Existing value:', my_dict["Sasha"]) #Выведите на экран одно значение по существующему ключу
print('Not existing value:', my_dict.get("Salima")) # Выведите на экран одно значение по  отсутствующему из словаря my_dict без ошибки.
my_dict.update({"Natasha" : 1985,
                "Varya" : 2019}) #Добавьте ещё две произвольные пары того же формата в словарь
print(my_dict)
Deleted_value = my_dict.pop ("Natasha") #Удалите одну из пар в словаре по существующему ключу из словаря my_dict

print('Deleted value:', Deleted_value) #  выведите значение из этой пары на экран.
print('Modified dictionary:', my_dict)

my_set={1, 2, 3, 2, 1, 'Яблоко', 'Груша', 'Яблоко', 'Груша', 42.314}
print('Set:', my_set) #- Выведите на экран множество my_set (должны отобразиться только уникальные значения)
my_set.add('Sting')
my_set.add('float') #Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
print(my_set)
my_set.discard(42.314) #Удалите один любой элемент из множества my_set.
print('Modified set:', my_set) #Выведите на экран измененное множество my_set.




