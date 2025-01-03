# ⭐Задачник. День 4

# 🚀 Задача 1: Калькулятор расхода топлива
# fuel = int(input("Введи количество топлива в баке: "))
# fuel_per_100km = int(input("Введи расход топлива на 100 км: "))
# distance = int(input("Введи расстояние, которое нужно проехать в км: "))
#
# distance_km = (distance / 100) * fuel_per_100km
# fuel_left = fuel - distance_km # Хватит ли бака
# if fuel_left < 0:
#     print('Не хватит топлива')
# else:
#     print('Топлива хватит')
#
# print(f'Для преодоления дистанции нужно {distance_km} литров топлива')


# 🧮 Задача 2: Конвертер единиц измерения
#**Описание**: Создайте конвертер единиц измерения, который позволяет пользователю ввести количество в одной единице (например, метры)
# и выбрать в какие единицы измерения он хочет конвертировать (например, футы, ярды, дюймы).
# Программа должна вывести результат конвертации.

# meters = int(input("Введите количество метров: "))
# convert = input("В какую единицу измерения хотите конвертировать? (футы, ярды, дюймы): ")
#
# if 'фут' in convert:
#     print(f'{meters} метров = {meters * 3.28084} футов')
# elif 'ярд' in convert:
#     print(f'{meters} метров = {meters * 1.09361} ярдов')
# elif 'дюйм' in convert:
#     print(f'{meters} метров = {meters * 39.3701} дюймов')
# else:
#     print('Вы ввели неверное значение')


## 📅 Задача 3: Дни недели
# **Описание**: Попросите пользователя ввести номер дня недели (1 для понедельника, 2 для вторника и так далее).
# Программа должна вывести соответствующий день недели в текстовом виде.

# day = int(input("Введите номер дня недели,
# 1 - понедельник, 2 - вторник, 3 - среда, 4 - четверг, 5- пятница, 6 - суббота, 7 - воскресенье: "))
# if day == 1:
#     print('Понедельник')
# elif day == 2:
#     print('Вторник')
# elif day == 3:
#     print('Среда')
# elif day == 4:
#     print('Четверг')
# elif day == 5:
#     print('Пятница')
# elif day == 6:
#     print('Суббота')
# elif day == 7:
#     print('Воскресенье')
# else:
#     print('Вы ввели неверное значение')

## 🌡️ Задача 4: Конвертер температуры

# **Описание**: Создайте программу, которая позволяет пользователю ввести температуру в градусах Цельсия и выбрать,
# в какую единицу измерения он хочет конвертировать (например, Фаренгейты, Кельвины). Программа должна вывести результат конвертации.

# temp = int(input("Введите температуру в градусах Цельсия: "))
# convert = input("В какую единицу измерения конвертировать (Фаренгейты - 1, Кельвины - 2): ")
#
# if 'Фаренгейт' in convert:
#     print(f'{temp} градусов Цельсия = {temp * 1.8 + 32} градусов Фаренгейта')
# elif int(convert) == 1:
#     print(f'{temp} градусов Цельсия = {temp * 1.8 + 32} градусов Фаренгейта')
# elif 'Кельвин' in convert:
#     print(f'{temp} градусов Цельсия = {temp + 273.15} градусов Кельвина')
# elif int(convert) == 2:
#     print(f'{temp} градусов Цельсия = {temp + 273.15} градусов Кельвина')
# else:
#     print('Вы ввели неверное значение')

## 🎂 Задача 5: Определение года рождения

# **Описание**: Попросите пользователя ввести свой возраст и определите, в каком году он родился. Учтите текущий год при расчете.

# age = int(input("Введи свой возраст: "))
# year = 2024 - age
# print(f'Ты родился в {year} году')

## 📧 Задача 6: Проверка адреса электронной почты

# **Описание**: Попросите пользователя ввести адрес электронной почты и проверьте, является ли этот адрес валидным
# (содержит символ "@" и точку после "@"). Выведите результат проверки.

# email = input('Введи адрес электронной почты: ')
# if '@' in email:
#     if '.' in email:
#         print('Адрес электронной почты валиден')
#     else:
#         print('Адрес электронной почты не валиден')
# else:
#     print('Адрес электронной почты не валиден')

## 🎬 Задача 7: Подсчет слов в предложении

# **Описание**: Попросите пользователя ввести предложение, а затем подсчитайте количество слов в этом предложении.
# Слова разделяются пробелами.

# text = input("Введи предложение, а я посчитаю слова в нём: ").split()
# text_symbol = len(text)
# print(text)

## 💡 Задача 8: Проверка на палиндром

# **Описание**: Попросите пользователя ввести слово или фразу, а затем проверьте, является ли это слово или фраза палиндромом
# (читается одинаково слева направо и справа налево). Выведите результат проверки.

# text = input('Введи слово, проверю его на палиндром: ').lower()
# reverse_text = text[::-1]
# if text == reverse_text:
#     print(f'Слово {text} является палиндром')
# else:
#     print(f'Слово {text} не является палиндром')

## 🍔 Задача 9: Расчет суммы заказа в ресторане

# **Описание**: Создайте программу, она позволяет пользователю ввести стоимость
# блюда в ресторане и процент чаевых, которые он хочет оставить. Программа должна

#  вычислить общую сумму заказа, включая чаевые.

# value = int(input('Введи стоимость заказа: '))
# percent = int(input('Введи процент чаевых: '))
# sum_percent = value * (percent / 100)
# sum_value = value + sum_percent
# print(f'Общая сумма заказа с учётом чаевых: {sum_value}')

## 🌧️ Задача 10: Погода

# **Описание**: Попросите пользователя ввести текущую температуру и условия погоды (например, "солнечно", "дождь").
# В зависимости от введенных данных, программа должна дать рекомендацию, как одеться.

# temp = float(input('Введи температуру: '))
# weather = input('Введи условия погоды (например, "солнечно", "дождь"): ')
# if weather == 'солнечно' and temp > 20:
#     print('На улице солнечно и тепло, одевайся полегче')
# elif weather == 'солнечно' and temp < 20:
#     print('На улице солнечно, но температурка не супер, одевай кофту')
# elif weather == 'дождь' and temp > 20:
#     print('На улице дождь, бери зонт, благо тепло')
# elif weather == 'дождь' and temp < 20:
#     print('На улице дождь, одевайся потеплее')
# else:
#     print('Введи условия погоды (например, "солнечно", "дождь"): ')

## 🎥 Задача 11: Оценка фильма

# **Описание**: Попросите пользователя ввести оценку фильма по шкале от 1 до 5.
# В зависимости от введенной оценки, программа должна вывести текстовое описание оценки
# (например, "Отличный фильм!" или "Плохой фильм!").

# name_film = input('Введи название фильма: ')
# score_film = int(input('Введи оценку фильма (от 1 до 5): '))
# if score_film == 1:
#     print(f'Ты поставил - {score_film}, фильму "{name_film}", значит фильм так себе')
# elif score_film == 2:
#     print(f'Ты поставил - {score_film}, фильму "{name_film}", значит фильм ну такое')
# elif score_film == 3:
#     print(f'Ты поставил - {score_film}, фильму "{name_film}", значит фильм нормуль')
# elif score_film == 4:
#     print(f'Ты поставил - {score_film}, фильму "{name_film}", значит фильм хороший')
# elif score_film == 5:
#     print(f'Ты поставил - {score_film}, фильму "{name_film}", значит фильм очень классный')
# else:
#     print('Неправильная оценка попробуй ещё раз и введи число от 1 до 5 :)')

