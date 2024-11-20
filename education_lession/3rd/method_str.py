# - `upper()`: преобразует все символы строки в верхний регистр.
# - `lower()`: преобразует все символы строки в нижний регистр.
# - `capitalize()`: преобразует первый символ строки в верхний регистр, а все остальные символы в нижний регистр.
# - `split()`: разделяет строку на подстроки, используя заданный разделитель, и возвращает список подстрок.
# - `join()`: соединяет строки из списка, используя данную строку в качестве разделителя.
# - `replace()`: заменяет все вхождения заданной подстроки на другую подстроку.
# - `strip()`: удаляет все начальные и конечные пробелы из строки.

text = "Hello World!"
index = 1
# print(index, text.upper())

fruits = "grapefruit,apple,banana"
# print(str.split(","))

color = ["green", "blue", "red"]
test_join = ", ".join(color)
# print(test_join)

replace_text = "Hello World!"
after_replace = replace_text.replace("World", "Python")
# print(after_replace)


json = {
    "name": "John",
    "age": 30,
    "city": "New York   "
}
# json_str = str(json)
# json_str_replace = json_str.replace(" ", "").replace(":", ": ").replace("{", "").replace("}", "").replace("'", "").replace(",", "\n")
# print(json_str_replace)


for char in range(0, 100):
        print(char)
print(json)
