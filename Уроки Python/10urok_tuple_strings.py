# list
# tuple

# numbers = [10, 20, 30, 40, 50]
# mix = [10, 20, True, "qwerty", 3,14]
# names = ["Diana", "Dias", "Mansur"]
# #          0   1   2   3   4
# print(numbers[0])
# print(numbers[-1])
# print(numbers[-2])

# numbers = [10, 20, 30, 40, 50]
# numbers[0]= "qwerty"
# numbers.append(40)
# numbers.insert(4,40)

# Задача 1 (разогрев) 
# Дан список nums = [5, 2, 9, 1, 7]
# Выведите первый и последний элементы 
# Отсортируйте список по возрастанию 
# Выведите длину списка
# nums = [5, 2, 9, 1, 7]
# print(nums[0], nums[-1])
# nums.sort()
# print(nums)
# len = len(nums)
# print(len)

# Дан список a = [10, 20, 30, 40]
# Замените второй элемент на 999, добавьте в конец число 111 и удалите первый элемент.
# a = [10, 20, 30, 40]
# a[2] = 999
# a.append(111)
# a.pop(0)
# print(a)

# Пользователь вводит 5 чисел (по одному).
# Сохраните их в список и выведите сумму.
# list = []
# for i in range(5):
#     a = int(input("Enter a number: "))
#     list.append(a)
# print(list)
# print(sum(list))

# Дан список оценок:
# grades = [50, 90, 75, 100, 60, 88]
# Найти максимальную оценку
# Посчитать среднюю
# Сколько оценок ≥ 80?

# grades = [50, 90, 75, 100, 60, 88]
# print(max(grades))
# print(sum(grades)/len(grades))
# a=0
# for i in grades:
#     if i>=80:
#         a+=1
# print(a)

# Для списка заказов
# [id, цена]: найдите сумму:
# минимальную сумму и id

# orders = [
#     [301, 5000],
#     [302, 12000],
#     [303, 2000],
#     [304, 10000],
#     [305, 990],
# ]

# total =0
# for i in orders:
#     total += i[1]

# min_price = orders[4][1]
# min_id = orders[0][0]

# for i in orders:
#     order_id = i[0]
#     price = i[1]

# if price < min_price:
#     min_price = price
#     min_id = order_id

# print(total)
# print(min_price)
# print(min_id)

# tuple - КОРТЕЖИ
# numbers = (10, 20, 30)
# print(numbers[0])

# Индексы и срезы одинаковые

# tuple = (10, 20, 30, 40, 50)
# print(tuple[0])
# print(tuple[-1])
# print(tuple[1:3])









# --------------------------------------------------СТРОКИ----------------------------------------------------------

# a ="qwerty"
# for i in a:
#     print(i)

# text = "python"
# print(text[0])
# print(text[-1])
# print(len(text))

# text = "python"
# print(text[0:2])
# print(text[2:5])
# print(text[3:])
# print(text[:3])
# print(text[::-1])

# name = "dIaS"
# print(name.lower())
# print(name.upper())
# print("hello world".title())
# print(name.capitalize())

# name = input("Enter a name: ")
# clean_name = name.strip().lower().capitalize()
# print("Hello", clean_name)

# text = "I like JS. JS is cool!"

# new_text = text.replace("JS", "python")
# print(new_text)

# text = "hello world everuthing is good "
# print(text.replace(" ", "_"))

# text = "I love Python lang prog"
# words = text.split()
# print(words)
# print(len(words))

# data = "Dias 18 95"
# parts = data.split(" ")
# print(parts)

# words = ["I", "hate", "C++"]
# words2 = " ".join(words)
# print(words2)

# in / find()
# text = "Hello World"
# print("World" in text)
# print("cat" in text)

# print(text.find("World"))
# print(text.find("cat"))
# print(text.find("l"))




# lower() -> строчные буквы
# upper() -> КАПСЛОК
# capitalize() -> Нормальный вид текста
# strip() -> убирает пробелы, удаляет
# lstrip() ->
# rstrip() ->
# find() -> находит элемент, пишет индекс
# title() -> нормальный вид текста как в предложения
# join() -> из массива в текст
# split() -> из текста в массив
# replace() -> Заменяем значение на нужное (Что менять, На что хотим поменять)



# 1.Пользователь вводит своё имя.
# Выведите Привет, <Имя>!, где имя приведено к нормальному виду (первая буква заглавная, лишние пробелы убраны).
# name = input("Enter a name: ")
# clean_name = name.strip().lower().capitalize()
# print("Hello", clean_name)

# 2.Пользователь вводит строку.
# Выведите:
# количество символов
# количество пробелов
# text = input("Enter a text: ")
# len = len(text)
# spaces = 0
# for i in text:
#     if i == " ":
#         spaces+=1
# print(len)
# print (spaces)


# 3.Пользователь вводит предложение.
# Выведите количество слов.
# text = input("Enter a text: ")
# list = text.split()
# print(len(list))


# 4.Пользователь вводит строку.
# Сделайте так, чтобы:
# все буквы были маленькими
# все пробелы заменены на _
# text = input("Enter a text: ")
# print(text.lower().replace(" ", "_"))


# 5.Пользователь вводит слово.
# Посчитайте, сколько в нём гласных букв (а, о, е, ё, и, ы, у, ю, я).

word = input("Enter a word: ")
vowels = "аоеёиыуюя"
count = 0
for i in word:
    if i in vowels:
        count+=1
print(count)
