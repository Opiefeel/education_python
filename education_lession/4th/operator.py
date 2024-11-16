# x = 1
# y = -1
# if x > 0 and y > 0:
#     print("Числа положительные, гуд :)")
# else:
#     print("Где-то есть отрицательное число :(")
#
# text = input("Введите текст: ")
# if text.isalpha():
#     print("Строка содержит только буквы")
# elif text.isdigit():
#     print("Строка содержит только цифры")
# else:
#     print("Строка содержит и буквы и цифры")

# Упрощённый вариант использования if

# a = 2
# if a: # проверка на true или false (то есть пустая или нет)
#     print("Строка не пустая")
# else:
#     print("Строка пустая") # Например, если передадим 0 в переменной a

# in - проверка на вхождение в список, логический оператор

# typical_cat = '''Барсик был очень пушистым котом. Он любил сметану и рыбу.
# А ещё, он обожал спать. Он мог бы спать целыми днями.
# Если бы не сметана и рыба.'''
# if "кот" in typical_cat.lower():
#     print("Кажется в тексте у нас то речь про кота")
# elif "пес" in typical_cat.lower():
#     print("Мы тут имеем дело с псом")
# elif "попугай" in typical_cat.lower():
#     print("Оказывается, что это попугай")

# Если есть вариант, где должно быть несколько выводом, то пользуемся несколькими if

# if "пушист" in typical_cat:
#     print ("Барсик был пушистым")
# if "сметан" in typical_cat:
#     print ("Барсик любил сметану")
# if "рыб" in typical_cat:
#     print ( "Барсик любил рыбу")
# if "спат" in typical_cat:
#     print ( "Барсик любил спать")

# Давайте поговорим о погоде

# weather = input("Какая сейчас погода? ").lower()

# if "солнечн" in weather:
#     print("Пойдём на пляж")
# elif "дожд" in weather:
#     print("Пойдём в кино")
# elif "снег" in weather:
#     print("Пойдём кататься на лыжах")
# else:
#     print("Пойдём гулять")

graduation = input("Введи оценку от 1 до 10: ")

if not graduation.isdigit():
    print("Оценка должна быть числом")
    exit(1)
else:
    graduation = int(graduation)

if 0 <= graduation <= 1:
    print(f'Оценка {graduation} - ужас просто')
elif 1 < graduation < 3:
    print(f'Оценка {graduation} - это плохо')
elif 3 <= graduation < 5:
    print(f'Оценка {graduation} - это не очень')
elif 5 <= graduation < 7:
    print(f'Оценка {graduation} - это нормально')
elif 7 <= graduation < 9:
    print(f'Оценка {graduation} - это хорошо')
elif 9 <= graduation <= 10:
    print(f'Оценка {graduation} - это отлично')
else:
    print("Введите корректную оценку")
