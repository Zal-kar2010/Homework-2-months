# Определю гласные буквы
vowels = set("aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ")
consonants = set("bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщBCDFGHJKLMNPQRSTVWXYZБВГДЖЗЙКЛМНПРСТФХЦЧШЩ")

while True:
    word = input("Введите слово (или 'exit' для выхода): ").strip()
    if word.lower() == 'exit':
        print("Выход из программы.")
        break

    # Удалю все символы, которые не являются буквами
    letters = [char for char in word if char.isalpha()]
    total = len(letters)
    v_count = sum(1 for char in letters if char in vowels)
    c_count = sum(1 for char in letters if char in consonants)

    if total == 0:
        print("Нет букв в слове.")
        continue

    v_percent = round((v_count / total) * 100)
    c_percent = round((c_count / total) * 100)

    print(f"Слово: {word}")
    print(f"Количество букв: {total}")
    print(f"Согласных букв: {c_count}")
    print(f"Гласных букв: {v_count}")
    print(f"Гласные/Согласные: {v_percent}% / {c_percent}%\n")