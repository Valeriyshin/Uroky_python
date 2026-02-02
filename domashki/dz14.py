# Домашняя работа по теме «Вложенные функции в Python»
# Цель: закрепить понимание вложенных функций, области видимости и логики проверок.

# Общие требования:
# 1. Использовать вложенные функции
# 2. Вложенные функции не принимают аргументы
# 3. Использовать переменные внешней функции
# 4. Использовать return, print запрещён

# Задание 1. Регистрация пользователя
# Функция register_user(username, password).
# check_username() — имя не пустое
# check_password() — длина ≥ 8
# Результат: «Регистрация успешна» / «Ошибка регистрации»
def register_user(username, password):
    def check_username():
        return bool(username)

    def check_password():
        return len(password) >= 8

    if check_username() and check_password():
        return "Регистрация успешна"
    else:
        return "Ошибка регистрации"
print(register_user("user1", "qwerty123"))
print(register_user("", "short"))
print(register_user("user2", "short"))


# Задание 2. Проверка заказа
# Функция check_order(quantity, in_stock).
# check_quantity() — количество > 0
# check_stock() — товар в наличии
# Результат: «Заказ принят» / «Заказ отклонён»
    
def check_order(quantity, in_stock):
    def check_quantity():
        return quantity > 0

    def check_stock():
        return in_stock

    if check_quantity() and check_stock():
        return "Заказ принят"
    else:
        return "Заказ отклонён"
print(check_order(5, True))
print(check_order(0, True))
print(check_order(3, False))


# # Задание 3. Проверка оценки
# # Функция check_grade(score).
# # is_number() — значение число
# # is_valid_range() — от 0 до 100
# # Результат: «Оценка принята» / «Некорректная оценка»
def check_grade(score):
    def is_number():
        return isinstance(score, (int, float))

    def is_valid_range():
        return 0 <= score <= 100

    if is_number() and is_valid_range():
        return "Оценка принята"
    else:
        return "Некорректная оценка"
print(check_grade(85))
print(check_grade(150))
print(check_grade("A"))

# # Задание 4. Доступ к системе
# # Функция system_access(role, is_active).
# # check_role() — admin или manager
# # check_status() — активен
# # Результат: «Доступ открыт» / «Доступ запрещён»  
def system_access(role, is_active):
    def check_role():
        return role == "admin" or role == "manager"
    def check_status():
        return is_active == "active"
    if check_role() and check_status():
        return "«Доступ открыт»"
    else:
        return "«Доступ запрещён»"
    
print(system_access("admin", "active"))
print(system_access("manager", "inactive"))
print(system_access("user", "active"))

# # Задание 5. Проверка оплаты
# # Функция check_payment(amount, balance).
# # check_amount() — сумма > 0
# # check_balance() — баланс ≥ суммы
# # Результат: «Оплата прошла» / «Недостаточно средств»
def check_paymemt(amount, balance):
    def check_amount():
        return amount>0
    def check_balance():
        return balance>=amount
    if check_amount() and check_balance():
        return "«Оплата прошла»"
    else:
        return"«Недостаточно средств»"

print(check_paymemt(1000, 2000))
print(check_paymemt(0, 1000))
print(check_paymemt(1000, 200))



