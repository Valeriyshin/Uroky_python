# ДЗ №5
# Модуль 3. Циклы.
# Задание 1
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). 
# Требуется проанализировать все числа в этом диапазоне по следующему правилу: 
# если число кратно 7, его надо выводить на экран.
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

for i in range(num1, num2):
    if i%7==0:
        print(i)

# Задание 2
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.

num1 = int(input("Enter a start number: "))
num2 = int(input("Enter a end number: "))
count=0
for i in range(num1, num2+1):
    print(i , end=" ")
print()    
for i in range(num2, num1-1, -1):
    print(i, end=" ")
print()
for i in range(num1, num2+1):
    if i%7==0:
        print(i, end=" ")
print("")
for i in range(num1, num2+1):        
    if i%5==0:
        count+=1
        print(count, end=" ")
print(" ")

# Задание 3
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz. 
# Если число кратно 5 нужно вывести слово Buzz. 
# Если число кратно 3 и 5 нужно вывести Fizz Buzz. 
# Если число не кратно не 3 и 5 нужно вывести само число.

num1 = int(input("Enter a start number: "))
num2 = int(input("Enter a end number: "))

for i in range(num1, num2+1):
    if i%3==0 and i%5==0:
        print(i, "Fizz Buzz")
    elif i%3==0:
        print(i, "Fizz")
    elif i%5==0:
        print(i, "Buzz")
    else:
        print(i)
    
