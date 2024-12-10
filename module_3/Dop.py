data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]


def calculate_structure_sum(*data):
    numbers = 0
    for i in data:
        if isinstance(i, (list, tuple, set)):
            numbers = numbers + calculate_structure_sum(*i)
        elif isinstance(i, dict):
            numbers = numbers + calculate_structure_sum(*i.items())
        elif isinstance(i, int):
            numbers = numbers + i
        elif isinstance(i, str):
            numbers = numbers + len(i)
        elif i is None:
            pass
    return numbers


result = calculate_structure_sum(data_structure)

print(result)
