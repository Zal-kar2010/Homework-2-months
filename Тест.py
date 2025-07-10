# while True:
#     цвет = input("Введите цвет светофора (красный, желтый, зеленый) или 'выход' для завершения: ").strip().lower()
#
#     if цвет == "красный":
#         print("Стой!")
#     elif цвет == "желтый":
#         print("Жди!")
#     elif цвет == "зеленый":
#         print("Иди!")
#     elif цвет == "выход":
#         print("Выход из программы.")
#         break
#     else:
#         print("Неверный ввод. Пожалуйста, введите: красный, желтый, зеленый или выход.")
#

days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
expenses = []
for day in days:
    amount = float(input(f'Введите сумму за {day}: '))
    expenses.append(amount)

total = sum(expenses)
average = round(total / len(expenses), 1)

print(f"Общая сумма: {total}")
print(f"Среднее арифметическое: {average}")
