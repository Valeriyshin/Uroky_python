
# try:
#     print(5/0)
# except Exception as e:
#     print(e)

# try:
#     print(5/0)
#     number=int("ten")
# except (ZeroDivisionError, ValueError):
#     print("Ошибка преобразования или деления")
# except Exception as e:
#     print(e)

# try:
#     money=int(input("Enter amount of money: "))
#     if money < 0:
#         raise ValueError("Money can't be negative!")
# except Exception as e:
#     print (e)
# finally:
#     print("Finished")

# Циклы.
# x=0
# while x<10:
#     print("hello")
#     x+=1
# print(x)

# stop_loop=True
# x=0
# while True:
#     print("infinite loop")
#     x+=1
#     if x==10:
#         stop_loop=False

# a=int(input("Enter a number: "))  
# b=int(input("Enter another number: "))
# sum=0
# while a<=b:
#     print(a, end=" ")
#     sum+=a
#     a+=1
# print()
# print(sum)

# word="python programming"
# for i in word:
#     print(i*2, end=" ")

# print()

# for i in 1,2,3,4,5:
#     print (i)

# for i in range(1,11):
#     print (i,end=" ")

# for i in range (11):
#     print(i,end=" ")

# print()

# for i in range (1,11,3):
#     print(i*10,end=" ")

# print()
# for i in range (1000, 990, -1):
#     print(i,end=" ")

# task 1
# try:
#     number=int(input("Enter a number: "))
#     if number > 999999:
#         raise ValueError("Number is too big")
#     elif number <100000:
#         raise ValueError("Number is too small")

#     num1=number//100000%10
#     num2=number//10000%10
#     num3=number//1000%10
#     num4=number//100%10
#     num5=number//10%10
#     num6=number%10

#     if num1+num2+num3==num4+num5+num6:
#         print("Lucky number")
#     else:
#         print("Not a lucky number")
# except Exception as e:
#     print(e)

#task 2
# try:
#     number=int(input("Enter a number: "))
#     if number > 999999:
#         raise ValueError("Number is too big")
#     elif number <100000:
#         raise ValueError("Number is too small")

#     num1=number//100000%10
#     num2=number//10000%10
#     num3=number//1000%10
#     num4=number//100%10
#     num5=number//10%10
#     num6=number%10
    
#     total_number=num6*100000+num5*10000+num3*1000+num4*100+num2*10+num1
#     print(total_number)
# except Exception as e:
#     print(e)

# try:
#     number=int(input("Enter a number of month: (1/2/3...)"))
#     if number > 12:
#         raise ValueError("Number is too big")
#     elif number < 1:
#         raise ValueError("Number is too small")
#     elif number==1 or number == 2 or number == 12:
#         print("Winter")
#     elif number ==3 or number== 4 or number== 5:
#         print ("Spring")
#     elif number == 6 or number== 7 or number==8:
#         print ("Summer")
#     elif number == 9 or number==10 or number==11:
#         print ("Autumn")
# except Exception as e:
#     print(e)

# if number==1 or number==2
# if number in (1,2,3)

# for i in range(1,11):
#     print (i)
#     for g in range(1,6):
#         print("i==", i, "g==", g)

# for i in range (1,11):
#     for g in range (1,6):
#         print(i*g, end="\t")
#     print()

# for i in range(1,11):
#     for j in range(1,6):
#         for k in range(1,11):
#             print(i,j,k)

# task2
# a=int(input("Enter a first number: "))
# b=int(input("Enter a second number: "))
# for i in range (a,b):
#     if i%2==1:
#         print(i, end= " ")

# task3
# a=int(input("Enter a first number: "))
# b=int(input("Enter a second number: "))
# for i in range (a,b):
#     if i%2==0:
#         print(i, end= " ")

# task4
# a=int(input("Enter a first number: "))
# b=int(input("Enter a second number: "))
# if a > b:
#     for i in range (a,b, -1):
#         print(i, end= " ")
# elif b > a:
#     for i in range (b,a, -1):
#         print(i, end= " ")

# task5
# a=int(input("Enter a first number: "))
# b=int(input("Enter a second number: "))
# if a > b:
#     for i in range (b,a+1):
#         if i%2==1:
#             print(i, end= " ")
# elif b > a:
#     for i in range (a,b+1):
#         if i%2==1:
#           print(i, end= " ")