class Person:
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def get_occupation(self):
        return self.__occupation

    def has_higher_education(self):
        return self.__higher_education

    def introduce(self):
        edu = "есть высшее образование" if self.__higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. У меня {edu}.")


class Friend(Person):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, hobby: str):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu = "есть высшее образование" if self.has_higher_education() else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.get_occupation()}. Мое хобби {self.hobby}. У меня {edu}.")


class Classmate(Person):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, group: str):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        edu = "есть высшее образование" if self.has_higher_education() else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.get_occupation()}. Я учился с Игорем в группе {self.group}. У меня {edu}.")


# Примеры
cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()

