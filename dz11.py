# # Домашнее задание по словарям (средний уровень)
# # 1. Дан словарь товаров {"apple": 120, "banana": 80, "orange": 150}. Вывести название товара с минимальной ценой.
dict = {
    "apple": 120, 
    "banana": 80,
    "orange": 150
}
min_price=min(dict.values())
for i,j in dict.items():
    if j == min_price:
        print(i)

# 2. Дан словарь студентов {"Dias": 78, "Madina": 92, "Aruzhan": 85}. Вывести всех студентов, у которых балл больше 80.

dict_students = {
    "Dias": 78,
    "Madina": 92,
    "Aruzhan": 85
}
for name, score in dict_students.items():
    if score > 80:
        print(name)

# 3. Дан словарь {1: "a", 2: "b", 3: "c"}. Создать новый словарь, где ключи и значения поменяны местами.

dict= {
    1: "a",
    2: "b",
    3: "c"
}
new_dict = {}
for key, value in dict.items():
    new_dict[value] = key

print(new_dict)

# 4. Дан словарь пользователя {"name": "Dias", "age": 17}. Если ключ "premium" отсутствует — добавить его со значением False.
dict = {
    "name": "Dias",
    "age": 17
}

if "premium" not in dict:
    dict["premium"] = False
print(dict)
# 5. Дан словарь {"a": 1, "b": 2, "c": 3}. Подсчитать количество ключей без использования len().
dict = {
    "a": 1,
    "b": 2,
    "c": 3
}
count = 0
for key in dict:
    count += 1
print(count)

# 6. Дан словарь товара {"apple": 5, "banana": 0, "orange": 3}. Уменьшить количество каждого товара на 1, если оно больше нуля.

dict = {
    "apple": 5,
    "banana": 0,
    "orange": 3
}
for key, value in dict.items():
    if value > 0:
        dict[key] = value - 1
print(dict)
# 7. Дан словарь координат {"x": 10, "y": 20, "z": -5}. Увеличить каждую координату в 2 раза.
dict = {
    "x":10,
    "y":20,
    "z": -5
}
for i in dict:
    dict[i] = dict[i] * 2
print(dict)
# 8. Дан словарь оценок ученика {"math": 90, "python": 100, "english": 85}. Вывести среднее арифметическое.
dict = {
    "math": 90,
    "python": 100,
    "english": 85
}
average = sum(dict.values()) / len(dict)
print(average)

# 9. Дан список слов ["apple", "banana", "apple", "orange"]. 
# Создать словарь, где ключ — слово, значение — количество повторений.

words = ["apple", "banana", "apple", "orange"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
# 10. Дан словарь пользователей: {1: {"name": "Dias", "role": "admin"}, 2: {"name": "Arman", "role": "user"}}. 
# Вывести только имена пользователей с ролью admin.
users = {
    1: {"name": "Dias", "role": "admin"},
    2: {"name": "Arman", "role": "user"}
}
for user_id, user_info in users.items():
    if user_info["role"] == "admin":
        print(user_info["name"])