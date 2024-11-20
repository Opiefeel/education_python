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

menu = ['продукты', 'акции', 'товары']
print("Меню:")

for item, value in enumerate(menu, start=1):
    print(f'{item}. {value}')


