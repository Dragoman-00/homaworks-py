numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустой список для простых чисел
prime_numbers = []

# Перебираем список номеров
for num in numbers:
    # Предположим, что число простое
    is_prime = True
    # Проверяем, делится ли число на любое число от 2 до самого числа
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    # Если число простое, добавить его в список prime_numbers
    if is_prime:
        prime_numbers.append(num)

# Выводим простые и непростые числа
print("Primes:", prime_numbers)
print("Not Primes:", [num for num in numbers if num not in prime_numbers])