def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {num}")
    return result, incorrect_data


def calculate_average(numbers):
    if isinstance(numbers, str):
        # Если numbers является строкой, обрабатываем каждый символ отдельно
        numbers = list(numbers)

    if not isinstance(numbers, (list, tuple, set)):
        # Если numbers не является списком, кортежем или множеством, выводим сообщение и возвращаем None
        print("В numbers записан некорректный тип данных")
        return None

    sum_result, incorrect_data = personal_sum(numbers)

    # Проверяем, сколько корректных чисел было
    valid_numbers_count = len([num for num in numbers if isinstance(num, (int, float))])

    if valid_numbers_count == 0:
        return 0  # Если нет корректных чисел, возвращаем 0

    return sum_result / valid_numbers_count


# Пример использования:
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Ожидается 0
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Ожидается 2.0
print(f'Результат 3: {calculate_average("1, 2, 3")}')  # Ожидается None
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Ожидается 26.5