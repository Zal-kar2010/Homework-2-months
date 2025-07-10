def guess_number():
    low = 1
    high = 100
    attempts = 0
    guesses = []

    print("Загадайте целое число от 1 до 100, а я попробую его угадать.")
    print("Отвечайте: 'да', 'больше', 'меньше'.")

    while True:
        if low > high:
            print("Что-то пошло не так. Возможно, вы дали противоречивые ответы.")
            break

        guess = (low + high) // 2
        guesses.append(guess)
        attempts += 1
        print(f"Моя попытка №{attempts}: это {guess}?")

        answer = input("Ваш ответ (да/больше/меньше): ").strip().lower()

        if answer == "да":
            print(f"Я угадал число {guess} за {attempts} попыток!")
            with open("results.txt", "w", encoding="utf-8") as file:
                file.write(f"Загаданное число: {guess}\n")
                file.write(f"Количество попыток: {attempts}\n")
                file.write(f"Список попыток: {guesses}\n")
            break
        elif answer == "больше":
            low = guess + 1
        elif answer == "меньше":
            high = guess - 1
        else:
            print("Пожалуйста, введите только 'да', 'больше' или 'меньше'.")