numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    is_prime = True
    for devizor in range(2, number):
        if number % devizor == 0:
            not_primes.append(number)
            is_prime = False
            break
    if is_prime == True and number != 1:
        primes.append(number)
print("Простые числа:", primes)
print("Не простые числа:", not_primes)
