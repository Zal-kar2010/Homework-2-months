data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

# строки → letters, остальное → numbers
for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    else:
        numbers.append(item)

# убираю 6.13, True в letters
numbers.remove(6.13)
numbers.remove(True)
letters.append(True)

# вставляю 2 между 3 и 1
index_1 = numbers.index(1)
numbers.insert(index_1, 2)

# сортировка и реверс
numbers.sort()
letters.reverse()

# заменяю 'g' на 'G', 'C' на 'c'
letters = ['G' if ch == 'g' else 'c' if ch == 'C' else ch for ch in letters]

# числа в квадрат
numbers = [x**2 for x in numbers]

# списки → кортежи
letters = tuple(letters)
numbers = tuple(numbers)

print("letters:", letters)
print("numbers:", numbers)
