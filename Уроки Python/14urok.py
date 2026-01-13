# # # def outer():
# # #     def inner():
# # #         print("Я внутри!")
# # #     inner()

# # # def check_price(price):
# # #     return price>0

# # # def add_product(products, name, price):
# # #     if not check_price(price):
# # #         print("Ошибка цены")
# # #         return
# # #     products.append({"name":name, "price":price})

# # # def add_product(products, name, price):
# # #     def check_price(price):
# # #         return price>0
# # #     if not check_price(price):
# # #         print("Цена должна быть больше 0")
# # #         return
    
# # #     products.append({"name": name, "price": price})








# # def products_order(order):
# #     def validate():
# #         return len(order) > 0
# #     def calculate():
# #         total = 0
# #         for i in order:
# #             total+=i["price"]
# #         return total

# #     if not validate():
# #         print("Пустой заказ")
# #         return
    
# #     return calculate 






# # 1. Простая вложенная функция (база)
# # Задача:
# # Напиши функцию greet(), внутри которой есть вложенная функция say_hello(), выводящая Привет.
# # Требования:
# # say_hello() объявлена внутри greet
# # say_hello() вызывается из greet
# def greet():
#     def say_hello():
#         print("Hello!")
#     say_hello()
# greet()









# # 2. Передача аргументов во вложенную функцию
# # Задача:
# # Напиши функцию print_name(name), внутри которой есть функция inner(), выводящая:
# # Имя: <name>
# # Требования:
# # inner() использует переменную name из внешней функции
# # inner() не принимает аргументы напрямую
# def print_name(name):
#     def inner():
#         print("Имя: ", name)
#     inner()
# print_name("Valera")








# # 3. Вложенная функция с return
# # Задача:
# # Создай функцию square(num), внутри которой функция calc() возвращает квадрат числа.
# # Требования:
# # calc() возвращает значение
# # square() возвращает результат calc()
# def square(num):
#     def calc():
#         return num*num
#     return calc()
# print(square(4))









# # 4. Проверка числа через вложенную функцию
# # Задача:
# # Напиши функцию check_number(num) с вложенной функцией is_positive().
# # Логика:
# # is_positive() возвращает True, если num > 0
# # check_number() возвращает строку:
# # "Положительное" или "Отрицательное или ноль"
# def check_number(num):
#     def is_positive():
#         if num >0:
#             return ("Положительное")
#         else:
#             return("Отрицательно или ноль")
#     return(is_positive())
# print(check_number(4))
# print(check_number(-2))




# # 5. Счётчик вызовов (замыкание)
# # Задача:
# # Напиши функцию counter(), внутри которой есть вложенная функция add().
# # Логика:
# # при каждом вызове add() число увеличивается на 1
# # counter() возвращает функцию add
# # Подсказка:
# # Используй nonlocal.
# def counter(count):
#     def add():
#         return count +1
#     return add()
# count = 0
# count = counter(count)
# count = counter(count)
# count = counter(count)
# print(count)



# # 6. Калькулятор с вложенными функциями
# # Задача:
# # Создай функцию calculator(a, b), внутри которой есть функции:
# # add()
# # sub()
# # mul()
# # Требования:
# # каждая функция использует a и b
# # # calculator() возвращает словарь с результатами всех операций
# def calculator(a, b):
#     def add():
#         return (a+b)
#     def sub():
#         return a-b
#     def mul():
#         return a*b
    
#     return {
#         "Плюс": add(),
#         "Минус": sub(),
#         "Умножить": mul()
#     }
# print(calculator(10,5))







# # 7. Фильтрация списка (практика)
# # Задача:
# # Напиши функцию filter_even(numbers), внутри которой вложенная функция is_even(n).
# # Логика:
# # is_even() возвращает True, если число чётное
# # filter_even() возвращает список только чётных чисел
# def filter_even(numbers):
#     def is_even(numbers):
#         return numbers % 2 == 0
    
#     result = []

#     for i in numbers:
#         if is_even(i):
#             result.append(i)
#     return result
# print(filter_even([1,2,3,4,5,6,7,8]))



# # 8. Генератор приветствий (функция возвращает функцию)
# # Задача:
# # Создай функцию greeting(text), которая возвращает вложенную функцию.
# # Логика:
# # вложенная функция принимает имя
# # возвращает строку: <text>, <имя>!
# # Пример:
# # hello = greeting("Здравствуйте")
# # print(hello("Анна"))
# def greeting(text):
#     def say(name):
#         return text + ", " + name + "!"
#     return say
# hello = greeting("Здравствуйте")
# print(hello("Alex"))





# # 9. Проверка доступа (реальный кейс)
# # Задача:
# # Напиши функцию access_control(role) с вложенной функцией check().
# # Логика:
# # если роль "admin" → доступ разрешён
# # иначе → доступ запрещён
# # Требования:
# # check() использует role из внешней функции
# # access_control() возвращает результат check()
# def access_control(role):
#     def check():
#         if role == "admin":
#             return "Доступ разрешен"
#         else:
#             return "Доступ запрещен"
#     return check()
# print(access_control("admin"))
# print(access_control("user"))


# # 10. Мини-валидация формы (приближено к реальности)
# # Задача:
# # Напиши функцию validate_user(name, age).
# # Внутри:
# # check_name() → имя не пустое
# # check_age() → возраст ≥ 18
# # Результат:
# # если всё ок → "Доступ разрешён"
# # иначе → "Ошибка данных"
# def validate_user(name, age):
#     def check_name():
#         return name != ""
#     def check_age():
#         return age >= 18

#     if check_name() and check_age():
#         return "Доступ разрешен"
#     else:
#         return "Ошибка данных"
    
# print (validate_user("Ivan",20))
# print(validate_user("", 25))
# print(validate_user("Gosha", 15))







# Задача 1. Проверка логина и пароля
# Условие:
# Напиши функцию check_auth(login, password).
# Внутри функции должны быть две вложенные функции:
# check_login() — возвращает True, если login не пустой
# check_password() — возвращает True, если длина пароля не меньше 6
# Логика основной функции:
# если обе проверки успешны → вернуть "Вход выполнен"
# иначе → вернуть "Ошибка авторизации"
# Примеры вызова (не реализовывать вывод):
# check_auth("admin", "123456")
# check_auth("", "123456")
# check_auth("user", "123")
def check_auth(login, password):
    def check_login():
        return login != ""
    def check_password():
        return len(password)>=6
    
    if check_login() and check_password():
        return "Вход выполнен"
    else: 
        return "Ошибка авторизации"
    
print(check_auth("admin", "123456"))
print(check_auth("", "123456"))
print(check_auth("user", "123"))



# Задача 2. Проверка товара
# Условие:
# Напиши функцию validate_product(name, price).
# Внутри:
# check_name() — True, если название не пустое
# check_price() — True, если цена больше 0
# Логика:
# если всё корректно → "Товар добавлен"
# иначе → "Ошибка товара"
def validate_product(name, price):
    def check_name():
        return name != ""
    def check_price():
        return price >0
    
    if check_name() and check_price():
        return "Товар добавлен"
    else: 
        return "Ошибка товара"
    
print(validate_product("banana", 300))
print(validate_product("", 250))
print(validate_product("apple", 0))







# Задача 3. Проверка email
# Условие:
# Создай функцию validate_email(email).
# Внутри:
# has_at() — проверяет, есть ли символ "@"
# has_dot() — проверяет, есть ли символ "."
# Логика:
# если обе проверки True → "Email корректен"
# иначе → "Некорректный email"
def validate_email(email):
    def has_at():
        return "@" in email

    def has_dot():
        return "." in email

    if has_at() and has_dot():
        return "Email корректен"
    else:
        return "Некорректный email"

print(validate_email("email"))
print(validate_email("valeriy@mail.com"))
print(validate_email("valeriy.mail.com"))






# Задача 4. Проверка доступа к курсу
# Условие:
# Напиши функцию check_course_access(completed_lessons, exam_passed).
# Внутри:
# lessons_done() — True, если completed_lessons >= 10
# exam_done() — True, если exam_passed == True
# Логика:
# если обе проверки выполнены → "Курс завершён"
# иначе → "Доступ закрыт"
def check_course_access(completed_lessons, exam_passed):
    def lessons_done():
        return completed_lessons>=10
    def exam_done():
        return exam_passed==True
    
    if lessons_done() and exam_done():
        return "Курс завершён"
    else:
        return "Доступ закрыт"
    
print(check_course_access(15, True))
print(check_course_access(9, True))
print(check_course_access(15, False))



# Задача 5. Проверка возраста и согласия
# Условие:
# Напиши функцию check_permission(age, has_permission).
# Внутри:
# is_adult() — True, если возраст ≥ 18
# has_parent_permission() — True, если has_permission == True
# Логика:
# если хотя бы одно условие выполнено → "Доступ разрешён"
# иначе → "Доступ запрещён"