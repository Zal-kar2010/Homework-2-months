#Контекстный менеджер “with”, работа с файлами
# w - write, re-write (запесьб перепесать)
# a - add (дозапись)
# x - создание уникального файла
# r - read


with open('new_file.txt', 'r') as file:
    print(file.read())

# with open('new1.txt', 'x') as new_file:
#     new_file.write('новый файл')

with open('new_file.txt', 'a') as file:
    file.write('\n2222')

file = open('new_file.txt', 'w')
file.write('Star war 15.')
file.close()