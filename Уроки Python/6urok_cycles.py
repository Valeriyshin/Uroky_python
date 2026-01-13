# for i in range(1,10):
#     print(i) База циклов

# for i in range(1,20, 2):
#     print(i) Чисто четные

# for i in range(10,0, -1):
#     print(i) В обратную сторону

# text = "abaqwetasgdsfcvreg"
# sum = 0
# for i in text:
#     if i == "a":
#         sum +=1

# print("Количество букв 'a'", sum)

# i=10
# while i>=1:
#     print(i)
#     i -=1
# print("Start")


# total =0
# num = int(input("Enter a nuber (0 = Stop): "))
# while num != 0:
#     total +=num
#     num = int(input("Enter a number (0>= Stop): "))
# print("Summa: ", total)

# secret = 7
# attempt = int(input("Ugaday number: "))

# while attempt != secret:
#     print("Wrong")
#     attempt = int(input("Ugaday number: "))
# print ("Good boy")

# task1 - Сумма всех чисел от 1 до 50 включительно
# total = 0
# for i in range (1,51):
#     print(i, end=" ")
#     total +=i
# print("")
# print("Summa: ", total)

# # task2 - Сумма всех четных чисел от 1 до 100 включительно
# total = 0
# for i in range (1,101):
#     if i % 2 ==0:
#         print(i, end=" ")
#         total +=i
# print("")
# print("Summa: ", total)

# task3 - Найти количество отрицательных чисел -10 -> 5
# sum = 0
# for i in range(-10, 5):
#     if i < 0:
#         print(i, end= " ")
#         sum += 1
# print("")
# print(sum)

# break/continue/pass

# word ="kaboom"
# for i in word:
#     if i == "a":
#         print("Find a letter a")
#         break
# print("Look", i)

# for i in range (0, 10):
#     print(i)
#     if (i==4):
#         print("Stop!")
#         break
# print(i)

# while True:
#     num = int(input("Enter a number (negative number = Stop)"))

#     if num <0:
#         print("Cycle stopped")
#         break

#     print("Your number", num)

# secret = 5

# while True:
#     x = int(input("Ugaday number:"))
#     if x == secret:
#         print("Good boy")
#         break
#     print("Ne ugadal")

# for i in range(1,21):
#     if i %2 !=0:
#         continue
#     print("Четное", i)

# while True:
#     text = input("Введите текст ('stop' -> выход): ")

#     if text =="stop":
#         break


#     if text == "":
#         continue

#     print("U Enter", text)


# word = "programming"

# for i in word:
#     if i not in "aoeiyu":
#         continue
#     print("Гласная", i)


# for i in range(5):
#     if i == 3:
#         pass
#     print(i)


# print("Mini kassa")
# print("Enter a price. 'pay' -> Stop")

# total = 0

# while True:
#     data = input("Price: ")
#     if data=="pay":
#         break
#     if data =="":
#         continue

#     price = float (data)

#     if price < 0:
#         print("Price can't be less than 0")
#         continue

#     total+=price
#     print("Now summa: ", total)

# print("Now full price: ", total)

print("Меню")
print("Выберите пункт меню")
print("1 — Добавить товар")
print("2 — Показать общую сумму")
print("3 — Оплатить")
print("0 — Выход")
print("Выберите пункт:")
while True:
    total = 0 
    choice = input("Цифра: ")
    if choice =="0":
        break
    if choice =="":
        continue
    

    