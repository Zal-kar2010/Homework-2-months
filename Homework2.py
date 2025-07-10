# homework_2.py

class Person:
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, работаю {self.occupation}")


class Friend(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг Амира, я родился {self.birth_date}, работаю {self.occupation}")


class Classmate(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник Алихана, я родился {self.birth_date}, работаю {self.occupation}")


# Создание объектов
friend1 = Friend(name="Тариэл", birth_date="5.7.2009", occupation="Программист", higher_education=True)
friend2 = Friend(name="Залкар", birth_date="30.10.2010", occupation="не работаю", higher_education=False)

classmate1 = Classmate(name="Бектур", birth_date="5.12.2010", occupation="Программист", higher_education=True)
classmate2 = Classmate(name="Айдар", birth_date="12.03.2011", occupation="не работаю", higher_education=False)

# Вызов методов introduce()
friend1.introduce()
friend2.introduce()
classmate1.introduce()
classmate2.introduce()