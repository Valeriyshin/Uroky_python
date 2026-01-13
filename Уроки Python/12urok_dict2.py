# person = {
#     "name": "Askar",
#     "age": 20,
#     "city": "Aktobe"
# }

# person["age"] = person["age"]+5
# print(person)


# students = [
#     {"name": "Ali", "score": 75},
#     {"name": "Adil", "score": 89},
#     {"name": "Era", "score": 95}
# ]
# for student in students:
#     if student["score"] >80:
#         print(student["name"])


# db = {
#     "python": {"students": 23, "teacher": "Adil"},
#     "js": {"students": 17, "teacher": "Dana"}
# }
# for key, info in db.items():
#     print (key+":", info["teacher"])



# Для каждой группы найти средний балл
# grades = {
#     "A": [90,80,70],
#     "B": [82, 71, 63],
#     "C": [57, 48]
# }
# for key, nums in grades.items():
#     avg = sum(nums)/len(nums)
#     print(key, "-", avg)

# # 5.
# orders = [
#     {"id":1, "price": 12000, "status": "paid"},
#     {"id":2, "price": 12000, "status": "pending"},
#     {"id":3, "price": 12000, "status": "paid"}
# ]
# # Найти сумму всех заказов со статусом "paid"
# total = 0
# for i in orders:
#     if i["status"] == "paid":
#         total += i["price"]
# print("Sum", total)

# users = [
#     {"name": "Ali", "role": "admin", "active": True},
#     {"name": "Adil", "role": "user", "active": False},
#     {"name": "Amir", "role": "user", "active": True}
# ]
# # Вывести имена только активных пользователей с ролью user
# for i in users:
#     if i["role"] == "user" and i["active"] == True:
#         print(i["name"])

# def hello():
#     print("Hello!")

# hello()

# def person(name):
#     print("Hello", name)

# person("Ali")


# def sum(a,b):
#     result = a+b
#     return result

# print(sum(3,4))

# def user(name, age, city):
#     print("Hello", name, age, city)

# user("Qwerty", 21, "Astana")

# def square(x):
#     return x*x
    
# print(square(2))

# def is_even(num):
#     if num%2 ==0:
#         return True
#     else:
#         return False
    
# print(is_even(4))
# print(is_even(7))

# def list_num(numbers):
#     total=0
#     for num in numbers:
#         total+=num
#     return total

# result = list_num((1,2,3,4,5))
# print(result)

# def format(person):
#     name = person["name"]
#     age = person["age"]
#     result = f"Name {name}, Age: {age}"
#     return result

# p = {"name": "Ali", "age": 21}
# print(p)





# Задача 1. Удалить пробелы
# Напиши функцию remove_spaces(text), которая:
# принимает строку
# возвращает строку без пробелов
# Пример:
# print(remove_spaces("he llo wo rld"))  # helloworld

# def remove_spaces(text):
#     result = ""
#     for i in text:
#         if i != " ":
#             result +=i
#     return result
# remove_spaces("qwe dfsg rge")
# print(remove_spaces("qwe dfsg rge"))

# ✅ Задача 2. Проверка возраста
# Напиши функцию can_enter(age), которая:
# принимает возраст
# если возраст ≥ 18 → вернуть "Allowed"
# иначе → "Denied"
# Пример:
# print(can_enter(20))  # Allowed
# print(can_enter(15))  # Denied


# def can_enter(age):
#     if age>=18:
#         return "Allowed"
#     else:
#         return "Denied"

# print(can_enter(13))


# ✅ Задача 3. Количество гласных в слове
# Напиши функцию count_vowels(word), которая:
# принимает строку
# возвращает количество гласных a, e, i, o, u (и их больших букв)
# Пример:
# print(count_vowels("Hello"))  # 2
# print(count_vowels("Sky"))    # 0

# def count(word):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for i in word:
#         if i in vowels:
#             count+=1
#     return count

# print(count("Skyler"))



# ✅ Задача 4. Разворот списка
# Напиши функцию reverse_list(lst), которая:
# принимает список
# возвращает новый список, где элементы идут в обратном порядке
# не использовать lst.reverse()
# Пример:
# print(reverse_list([1,2,3]))  # [3,2,1]

    


# ✅ Задача 5. Процент от числа
# Напиши функцию percent(number, percent), которая:
# принимает число и процент
# возвращает результат: какое значение составляет указанный процент от числа
# Пример:
# print(percent(200, 10))  # 20
# print(percent(150, 25))  # 37.5