# Знакомство со списками

# Списки - итерируемая, упорядоченная, изменяемая
# коллекция данных произвольных типов. Встроенный тип данных.

# Создание списка
# 1. Через литерал списка
# 2. Через вызов встроенной функции list()
# 3. Через генератор списка

# first_lst = [1, 2, 3, 4, 5]
# second_lst = list( "Hello, World!")
# third_lst = [i for i in range(10)]
#
# # Пустой список
# empty_lst = []
# empty_lst2 = list()
#
# shop_list = ['apple', 'banana', 'orange']
# if 'apple' in shop_list:
#     print("Apple is in the list")
#
# for item in shop_list:
#     print(item)
#
# menu = ['продукты', 'акции', 'товары']
# print("Меню:")
#
# for item, value in enumerate(menu, start=1):
#     print(f'{item}. {value}')

# Картавая задачка №2 с циклом for

# BAD_LETTER = 'ж'
# THRESHOLD = 2
#
# user_words = input('Я проанализирую введённые слова и верну список с результатам\n'
#                    'Введите слова через пробел: ').lower().split()
#
# result = []
#
# for word in user_words:
#     bed_letter_count = word.count(BAD_LETTER)
#     if bed_letter_count >= THRESHOLD:
#         result.append(word)
#
# if result:
#     print(f'Слова с буквой {BAD_LETTER} в количестве больше {THRESHOLD} или равно: {result}')
# else:
#     print('Таких слов нет')

# Создание списка продуктов с помощью for и range

# num_product = int(input('Введите количество продуктов: '))
# shop_list = []
#
# for i in range(num_product):
#     product = input(f'Введите название продукта {i + 1}: ').lower()
#     shop_list.append(product)
#
# print(f'Ваш список продуктов {list(enumerate(shop_list, start=1))}')

# Реализуйте функцию, которая возвращает самое часто встречаемое слово в слайсе (массиве).
# Если таких слов несколько, то возвращается первое из них

word_list = ["hello", "world", "my", "name", "is", "world", "hello", "my", "hello"]

for word in word_list:
    count = word_list.count(word)
    if count > 1:
        print(f'Слово {word} встречается {count} раза')
    else: break







