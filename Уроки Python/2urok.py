# print("Name: Valera\nFilm: Fight Club")

# name="Valera"
# age = 21
# height=1.70
# student=False

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(student))
# True=1
# False=0

# age=input("Ur age: ")
# age=int(age)
# print(age+1)

# name="Valera"
# age=21
# city="Almaty"

# print(f"Меня зовут {name}. Мне {age} лет. Я из города {city}.")

# \n
# age=int(input("ЭТО У МЕНЯ ИНТ"))
# age=str(age)
# f=амперсанд ""

# Задание 1: Перевод строки
# Выведи на экран информацию в виде анкеты:

# name = input("Введите имя: ")
# surname = input("Введите фамилию: ")
# age = int(input("Введите возраст: "))
# city = input("Введите город: ")
# address = input("Введите адрес: ")

# print("Name:\n", name, "\nSurname:\n", surname, "\nAge:\n", age, "\nCity:\n", city, "\nAddress:\n", address)

# Задание 2: Проверка типа

# Пусть пользователь введёт что-то, а ты покажи тип данных.

# data = input("Введите что-нибудь: ")
# print(type(data))

# Задание 3: f-строки
# Пусть программа приветствует пользователя:
# name=input("Введите имя: ")
# city=input("Введите город: ")
# print(f"Привет, {name}! Как погода в {city}?")

# Задание 4: Программа «Возраст»
# Пусть программа узнает год рождения и посчитает возраст.
# a=int(input("Write your year of birth: (format: 1990)"))
# b=2025
# print(f"You are {b-a} years old")

# Задание 5: Всё вместе
# Создай мини-анкету с форматированием и переносами строк

# name=input("Write your name: ")
# surname=input("Write your surname: ")
# age=int(input("Write your age: "))
# city=input("Write your city: ")
# address=input("Write your address: ")
# print(f"Name:\n{name}\nSurname:\n{surname}\nAge:\n{age}\nCity:\n{city}\nAddress:\n{address}")

# a=int(input("Write a number: "))
# if(a<10):
#     print("Ваше число меньше 10")
# else:
#     print("Ваше число больше 10")

# a=int(input("Write a number: "))
# if(a<0):
#     print("Ваше число отрицательное")
# else:
#     print("Ваше число положительное")

# a=int(input("Write a number: "))
# if(a%2==0):
#     print("Ваше число чётное")
# else:
#     print("Ваше число нечётное")

# Пользователь вводит число → программа пишет, положительное оно или отрицательное

# a=int(input("Write a number: :"))
# if(a>0):
#     print("Ваше число положительное")
# else:
#     print("Ваше число отрицательное")

# Пользователь вводит возраст → программа говорит, можно ли войти

# age=int(input("Write your age: "))
# if(age)==21:
#     print("Welcome!")
# else:
#     print("U r not enough age")

# Пользователь вводит имя и возраст → программа выводит приветствие через f-строку

# name=input("Write your name: ")
# age=int(input("How old are you?: "))
# if(name=="Valera" and age==21):
#     print("Hello, Valera! You are 21 years old!")
# else:
#     print("Wrong data")

# Бонус: пользователь вводит число → программа определяет, чётное ли оно

# a=int(input("Write a number: "))
# if(a%2==0):
#     print("Ваше число чётное")
# else:
#     print("Ваше число нечётное")

# Если пользователь из “Алматы” — особое приветствие.
# Иначе — стандартное.

# city=input("Write your city: ")
# if(city=="Almaty"):
#     print("Hello, mountain citizen!")
# else:
#     print("Hello, traveler!")

# Пользователь вводит имя и отвечает, есть ли у него билет (“да” или “нет”).
# Вывести результат с переносами строк и f-строкой.

# name=input("Write your name: ")
# ticket=input("Do u have a ticket? (yes/no): ")
# if(ticket=="yes"):
#     print(f"Welcome, {name}!\nWelcome to the club buddy!")
# else:
#     print(f"Sorry, {name}. Go fuck!")


# # Программа запрашивает имя и пароль.
# # Если пароль верный — выводит приветствие,
# # иначе — сообщение об ошибке.

# username=input("Write your name: ")
# password=int(input("Write a password: "))
# if(username=="Valera" and password==258003):
#     print("Hello, Valera! Have a good day!")
# else:
#     print("Wrong username or password")