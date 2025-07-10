# Функции: виды пораметров, возврашения данных, виды аргументов.
# Не повторяйся

"""из чего состоит функция"""

# определуние наименование(параметры)
#      тело функции
#      возвращение объекта
#
# вызов функции
# наименование (аргументов)


# def some_function(name, surname='неизвестно'): # required position parameter
#     print(f'name: {name}, surname: {surname}')
#
#
# some_function('zalkar', 'ert')
# some_function('bogdan')
# some_function(surname='aitmatov', name='chyngyz')

# def get_square(length: int, width:int) -> int:
#      """ Приминяет длину и ширину, возвращяет площать. """
#      square = length * width
#      return square
#
# print(get_square.__doc__)
# print(help(get_square))

# print(square_5)
# print(square_victory)


 def menu(**kwargs):
     return kwargs

 monday = menu(eat='pizza', drink='cola', rgw= 456, wfsa= 67)
 print(monday)

def plus(*args)
    return sum(args)


print(plus(2, 4, 2, 8))
print(plus(2431, 415, 253, 835))




# length = 10
# width = 5
# square_5 = length * width
# print(square_5)
#
# length = 450
# width = 240
# square_5 = length * width
# print(square_5)