def is_strong_password(password):
    if len(password) < 6:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = sum(1 for c in password if not c.isalnum()) >= 2

    return has_upper and has_lower and has_digit and has_special

# Ввод от пользователя
user_password = input("Введите пароль для проверки надежности: ")

if is_strong_password(user_password):
    print("Пароль надежный.")
else:
    print("Пароль ненадежный.")



def nearest_number(numbers, target=0):
    return min(numbers, key=lambda x: abs(x - target))

# Ввод от пользователя
user_input = input("Введите числа через пробел: ")
target_input = input("Введите целевое число (по умолчанию 0): ")

# Преобразуем строку в список чисел
numbers = [float(n) for n in user_input.split()]
target = float(target_input) if target_input.strip() else 0

result = nearest_number(numbers, target)
print(f"Ближайшее число к {target}: {result}")