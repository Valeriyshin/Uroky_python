# time=int(input("Введите время: "))
# ticket=False
# money=True
# luggage=False
# print((ticket or money) and not luggage and time>=6)

# car_speed=25
# if car_speed>60:
#     print("slow")
# elif car_speed>40:
#     print("medium")
# elif car_speed>20:
#     print("fast")

# Короткие команды лучше писать в одну строку, а условие писать через тернарный оператор
# age=int(input("Введите возраст: "))
# status="adult" if age>=18 else "child"
# print(status)

# odd=age if age %2==0 else 0
# print(odd)

# Как извлечь код из буквы и наоборот
# print("a">"A")
# print (")">"+")
# print(ord("a"))
# print(chr(65))

# name ="Valera"
# bool_valera=True if name=="Valera" else False
# print (bool_valera)

# num3=10
# if num3>15:
#     num4=10
# else:
#     num4=0
# print(num4)

# bank=int(input("Введите сумму в банке: "))
# if bank>0:
#     print("В банке:", bank)
#     human=int(input("Сколько вы хотите снять: "))
#     if human<=bank:
#         bank-=human
#         print("Вы сняли", human, "Остаток в банке:", bank)
#         human_again=int(input("Сколько вы хотите снять еще: "))
#         if human_again<=bank:
#             bank-=human_again
#             print("Вы сняли", human_again, "Остаток в банке:", bank)
#         else:
#             print("Недостаточно средств в банке")
#     else:
#         print("Недостаточно средств в банке")
# else:
#     print("Неверный счет")

# number=int(input("Enter a number: "))
# if number>0:
#     print("Greater than 0")
#     if number>10:
#         print("Greater than 10")
#         if number >20:
#             print("Greater than 20")
#         else:
#             print("Less than or equal to 20")




# seconds=int(input("Введите количество секунд прошедших с начала дня: "))
# choise=input("Для того чтобы узнать остаток времени, выберите тип данных (Часы, Минуты, Секунды): ")
# days_seconds=86400
# if choise=="Часы":
#     print("Остаток времени в часах:", (days_seconds-seconds)/3600)
# elif choise=="Минуты":
#     print("Остаток времени в минутах:", (days_seconds-seconds)/60)
# elif choise=="Секунды":
#     print("Остаток времени в секундах:", days_seconds-seconds)
# else:
#     print("Неверный тип данных")









# diameter=int(input("Введите диаметр окружности: "))
# choise=input("Вы хотите узнать площадь или периметр окружности? (Площадь/Периметр): ")
# if choise=="Площадь":
#     print("Площадь окружности:", 3.14*(diameter/2)**2)
# elif choise=="Периметр":
#     print("Периметр окружности:", 3.14*diameter)
# else:
#     print("Неверный тип данных")


# Исключения
# Case1

# try:
    # print(5/0)
    # print("hello"

    # print(5+9)
#     age=int(input("Введите ваш возраст: "))
# except:
#     print("Ошибка ввода данных. Введите число.")

# Case 2
# try:
#     age=int(input("Введите ваш возраст: "))
#     print("hello")
#     print(5+9)
# except Exception as error:
#     print(error)

# Задание 3
price=int(input("Enter price of PS5: "))
quantity=int(input("Enter quantity of PS5 (1-100): "))
percent=int(input("Enter a percent sale: "))
sale=percent/100
choice=int(input("Рассчитать стоимость заказа или одной приставки со скидкой? (1/2): "))
if choice == 1:
    print (price*quantity)
elif choice == 2:
    print (price-(price*sale))
else:
    print ("Error data")
