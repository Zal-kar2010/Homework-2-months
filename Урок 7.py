# # # Lambda функции. Обработка исключений;
from unittest import result

from Тест import expenses

# counter = 0
# expenses = {}
# while counter < 7:
#     try:
#         expenses = int(input('введите расход:'))
#         counter += 1
#         expenses[counter] = expenses
#         print(expenses)
#     except:
#         print('вводите только числа!')
#
# print(sum(expenses.values())/ len(expenses))





# try:
#     print(2 * 'q')
# except:
#     print('error found')
# else:
#     print('ok')
# finally:
#     print('проверка завершена')


#
# def def_func(n1, n2):
#     return n1 + n2
# print(def_func(2, 3))
# print(type(def_func))
#
# lamda_func = lambda n1, n2: n1 + n2
# print(lamda_func(2, 3))
# print(type(lamda_func))

# def up_first_letter(word: str) -> str:
#     return word.title()



# def show_word (func, word_list):
#     for word in word_list:
#         print(func(word))
#
# show_word(lambda word: word.title(), ['torogeldi', 'aisha'])

# show_word(up_first_letter, ['egor', 'bogdan', 'zalkar'])
# # show_word(len, ['tokmok', 'kant', 'karakol'])

# words = [
#     'torogeldi', 'aisha', 'egor', 'bogdan',
#     'abulkasym', 'zalkar', 'aisezim'
# ]
# print(words)
#
# map_words = list(map(lambda name: name.upper(), words))
# print(map_words)
#
# filter_words = list(filter(lambda name: 'a'in name, words))
# print(filter_words)
#
# sorted_words = sorted(words, key=lambda name: name[-1])
# print(sorted_words)


def nearest_number(numbers, target=0):
    return min(numbers, key=lambda x: abs(x - target))
print(nearest_number([12, 34, 76, 54, 89], 77))