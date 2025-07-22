from homeworks.distance import Distance

# Создаём объекты
d1 = Distance(300, 'см')  # 3.0 м
d2 = Distance(2, 'м')     # 2.0 м
d3 = Distance(0.001, 'км')  # 1.0 м

print("Инициализация:")
print(d1)
print(d2)
print(d3)

print("\nСложение:")
print(f"{d1} + {d2} = {d1 + d2}")

print("\nВычитание:")
print(f"{d1} - {d2} = {d1 - d2}")

print("\nСравнение:")
print(f"{d1} == {d2}: {d1 == d2}")
print(f"{d1} > {d3}: {d1 > d3}")
print(f"{d2} < {d3}: {d2 < d3}")

# Проверка на отрицательное вычитание
try:
    result = d2 - d3
    print(f"\nВычитание без ошибки: {result}")
except ValueError as e:
    print(f"\nОшибка при вычитании: {e}")
