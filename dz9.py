# Домашняя работа: Массивы и методы списков в Python
# 1.	1. Добавьте число 999 в конец списка с помощью метода append().
# nums = [10, 20, 30, 40, 50]
# nums.append(999)
# print(nums)

# 2.	2. Удалите из списка все элементы, равные 0, используя remove() и цикл while.
# nums = [1, 2, 5, 6, 0, 3, 0, 6, 2, 0]
# while 0 in nums:
#     nums.remove(0)
# print(nums)

# 3.	3. Посчитайте количество элементов со значением 5, используя count().
# nums = [1, 2, 5, 6, 0, 3, 0, 6, 2, 0, 5, 6, 4, 5]
# num_5= nums.count(5)
# print(num_5)

# 4.	4. Создайте новый список — перевёрнутую копию исходного.
# nums = [1, 2, 5, 6, 0, 3, 0, 6, 2, 0, 5, 6, 4, 5]
# reversed_nums = nums[::-1]
# print(reversed_nums)

# 5.	5. Разделите список на два: evens (чётные) и odds (нечётные).
# nums = [1, 2, 5, 6, 0, 3, 0, 6, 2, 0, 5, 6, 4, 5]
# evens = 0
# odds = 0
# for num in nums:
#     if num % 2 == 0:
#         evens += 1
#     else:
#         odds += 1
# print("Чётные:", evens)
# print("Нечётные:", odds)

# 6.	6. Удалите все числа меньше 10, используя pop() в цикле.
# nums = [1, 2, 5, 6, 0, 3, 10, 20, 30, 40, 50]
# while True:
#     for num in nums:
#         if num < 10:
#             nums.pop(nums.index(num))
#             break
#     else:
#         break
# print(nums)
# НЕПОНЯТНО, ПОЧЕМУ НЕ РАБОТАЕТ ЧЕРЕЗ FOR.

# 7.	7. Найдите три минимальных числа без изменения исходного списка.
# nums = [1, 2, 5, 6, 0, 3, 10, 20, 30, 40, 50]
# min_nums = sorted(nums)[:3]
# print(min_nums)

# 8.	8. Объедините два списка методом extend().
# nums = [1, 2, 5, 6, 0, 3]
# nums2 = [10, 20, 30, 40, 50]
# nums.extend(nums2) 
# print(nums)

# 9.	9. Найдите среднее значение списка и создайте список элементов, которые больше среднего.
# nums = [1, 2, 5, 6, 0, 3, 10, 20, 30, 40, 50]
# average = sum(nums) / len(nums)
# above_average = [num for num in nums if num > average]
# print("Среднее значение:", average)
# print("Элементы больше среднего:", above_average)

# 10.	10. Удалите все максимальные значения из списка.
# nums = [1, 2, 5, 6, 0, 3, 10, 20, 30, 40, 50]
# max_nums= nums.remove(max(nums))
# print(nums)

# 11.	11. Создайте новый список: сначала отрицательные числа, затем остальные.
# nums = [1, -2, 5, -6, 0, 3, -10, 20, 30, -40, 50]
# negatives = []
# positives = []
# for i in nums:
#     if i < 0:
#         negatives.append(i)
#     else:
#         positives.append(i)
# new_nums = negatives + positives
# print(new_nums)

# 12.	12. Для списка заказов [id, цена]: найдите сумму, минимальную цену и её id.
orders = [
    [301, 5000],
    [302, 12000],
    [303, 2000],
    [304, 10000],
    [305, 990],
]

total =0
for i in orders:
    total += i[1]

min_price = orders[4][1]
min_id = orders[0][0]

for i in orders:
    order_id = i[0]
    price = i[1]

if price < min_price:
    min_price = price
    min_id = order_id

print(total)
print(min_price)
print(min_id)
