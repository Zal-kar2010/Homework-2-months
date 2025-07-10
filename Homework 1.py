# homework_1.py

class Person:
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_status = "имею высшее образование" if self.higher_education else "не имею высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родился {self.birth_date}. "
              f"Я — {self.occupation}, и я {edu_status}.")

# Создаем объекты класса
person1 = Person("Залкар", "2010-10-30", "школьник", False)
person2 = Person("Джотаро Куджо", "1970-04-04", "стенд-юзер и морской биолог", True)
person3 = Person("Дио Брандо", "1867-05-13", "вампир", False)

# Печатаем атрибуты и вызываем метод introduce
for person in (person1, person2, person3):
    print(f"Имя: {person.name}")
    print(f"Дата рождения: {person.birth_date}")
    print(f"Профессия: {person.occupation}")
    print(f"Высшее образование: {person.higher_education}")
    person.introduce()
    print("-" * 40)
