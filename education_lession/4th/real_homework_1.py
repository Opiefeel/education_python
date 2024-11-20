# 🔏Валидатор паролей
#
# Привет!
#
# Вот мы и подошли к первому домашнему заданию 🎇
#
# Сегодня мы будем писать скрипт, который проверит пароль на надёжность. Мы изучили всё, что необходимо, для написания простого валидатора паролей.
#
# Мы будем проверять пароль на:
# - Длина не менее 8 знаков
# - Количество цифр не менее 1
# - Количество маленьких букв не менее 1
# - Количество больших букв не менее 1
#
# Все что вам нужно, это закончите этот код. (Заглушку `pass` из цикла можно убрать)

# Константы
THRESHOLD_DIGITS = 1
THRESHOLD_UPPER = 1
THRESHOLD_LOWER = 1
THRESHOLD_LEN = 8

# Cчетчики для проверки
digit_counter = 0
upper_counter = 0
lower_counter = 0

input_password = str(input("Введите пароль (все пробелы введённые в пароле будут удалены): ")).replace(" ", "")
sum_symbols = len(input_password)

for i in input_password:
    if i.isdigit():
        digit_counter += 1
    if i.isupper():
        upper_counter += 1
    if i.islower():
        lower_counter += 1

if digit_counter < THRESHOLD_DIGITS:
    print(f'В пароле нужна как минимум одна цифра')
elif digit_counter < THRESHOLD_UPPER:
    print(f'В пароле нужна как минимум одна маленькая буква')
elif upper_counter < THRESHOLD_LOWER:
    print(f'В пароле нужна как минимум одна большая буква')
elif sum_symbols <= THRESHOLD_LEN:
    print(f'Пароль должен содержать как минимум {THRESHOLD_LEN} символов')
else:
    print(f'Пароль "{input_password}" надежный, советую его записать :)')
