def nearest_number(numbers, target):
    sorted_list = sorted(numbers, key=lambda x: abs(x - target))
    return (target, sorted_list)

# Примеры:
print(nearest_number([312, 996, 31, 1991], 1000))
print(nearest_number([5, 20.18, 103, 4], 27))


# Пример с map возведение чисел в квадрат
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # [1, 4, 9, 16, 25]

# Пример с filter оставить только чётные числа
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]



def get_element_by_index(data=[1, 2, 3, 4, 5]):
    while True:
        user_input = input("Введите индекс элемента или 'exit' для выхода: ")
        if user_input.lower() == 'exit':
            break
        try:
            index = int(user_input)
            print(f"Элемент по индексу {index}: {data[index]}")
        except ValueError:
            print("Ошибка: Введите целое число.")
        except IndexError:
            print(f"Ошибка: Введите индекс от 0 до {len(data) - 1}.")

# Запуск функции
get_element_by_index()