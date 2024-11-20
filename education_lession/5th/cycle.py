# Знакомимся с циклом for
from importlib import import_module

# my_string = "Hello world!"

# for char in my_string:  # or letter in my_string
#     if char == "o":
#         print(char) # итерация

# my_string = "Hello world!"

# for char in my_string:  # or letter in my_string
#     print(char, end=" ")

# my_string = "Hello world! EEE!"
# count = 0
# for char in my_string:
#     if char.lower() == 'e':
#         count += 1
# print(f'Количество "e" в строке: {count}')

# my_string = "Hello world!"
# target_char = "Z"
#
# for char in my_string:
#     if char == target_char:
#         print(f'В {my_string} есть {target_char}')
#         break
# else:
#         print(f'В {my_string} нет {target_char}')

# string = "He2lloZ world!"
# target_char = "Z"
#
# for char in string:
#     if char.isdigit():
#         continue
#
#     if char == target_char:
#         print(f'В {string} есть {target_char}')
#         break
# else:
#     print(f'В {string} нет {target_char}')

# string = input("Тут проверяем на картавость, введи слово: ").lower()
# count_r = 0
#
# for char in string:
#     if char.lower() == "р":
#         print(f'Буква {char} - картавка')
#         count_r += 1
#     if count_r == 3:
#         print("Парень да тут 3 r, берегись")
#         break
# else:
#     print("Слово хорошее, меньше трех Р")