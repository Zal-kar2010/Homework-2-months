# имя
name = input("What your name: ").title()
# фамилия
surname = 'akimbaev'
age = int(input(f'{name}, plese enter your age: '))
height = 1.72
current_year = 2025
born = current_year - age
print(name, surname, age, height)
print(f'{name} {surname} {born} года рождения')
#print(name.title(), surname.upper(), age, height)

#print(type(age))
#print(type(height))