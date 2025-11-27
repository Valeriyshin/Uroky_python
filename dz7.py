# Домашка по вложенным циклам (Python)
# 1. Нарисовать прямоугольник N x M из символа '@'.
# n = int(input("Enter a lenght N: "))
# m = int (input("Enter a lenght M: "))
# for i in range (n):
#     print("")
#     for j in range (m):
#         print ("@",end="")
# print("")
# 2. Вывести треугольник высотой N (левая версия):
# *
# **
# ***
# n = int(input("Enter a lenght N: "))
# for i in range (n+1):
#     print("")
#     for j in range (i):
#         print ("@",end="")

# 3. Вывести перевёрнутый треугольник высотой N.
# n = int(input("Enter a lenght N: "))
# for i in range (n+1):
#     print("")
#     for j in range (n-i):
#         print ("@",end="")

# 4. Построить таблицу умножения от 1 до N.
# number = int(input("Enter a number N: "))
# for i in range (1, number+1):
#     print()
#     for j in range (1, number+1):
#         print (i*j, end="  |  ")
# print()

# 5. Нарисовать квадрат N x N, где рамка состоит из '*', а внутри пробелы.
# n = int(input("Enter N: "))

# for i in range(n):
#     if i == 0 or i == n - 1:
#         print("*" * n) 
#     else:
#         print("*" + " " * (n - 2) + "*")

# 6. Нарисовать квадрат с двумя диагоналями.
# N = int(input("Enter N: "))

# for i in range(N):
#     for j in range(N):
#         if i == 0 or i == N-1 or j == 0 or j == N-1 or i == j or j == N - 1 - i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# 7. Построить числовую лестницу:
# 1
# 12
# 123
# 1234
# n = int(input("Enter Number: "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


# 8. Построить правосторонний треугольник (с пробелами слева).
N = int(input("Enter N: "))

for i in range(1, N+1):
    print(" " * (N - i) + "*" * i)


# 9. Сгенерировать квадрат чисел от 1 до N*N.


# 10. Построить шахматную доску из '*' и пробелов.
N = int(input("Enter N: "))

for i in range(N):
    for j in range(N):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

