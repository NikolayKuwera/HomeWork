calls = 0  # Переменная для подсчета вызовов функций


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)


def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    lower_string = string.lower()  # Приводим все строки к нижнему регистру для сравнения
    return lower_string in (item.lower() for item in list_to_search)


# Примеры вызова функций
info = string_info("Capybara")

print("String Info:", info)

contains = is_contains("UrbaN", ["urban", "city", "town"])
print("Contains 'UrbaN' in list:", contains)

print("Total function calls:", calls)  # Вывод количества вызовов
