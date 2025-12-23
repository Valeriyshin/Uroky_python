# ЧАСТЬ 1. Добавить новую функцию
# ЗАДАНИЕ 1. Поиск товара по названию

# Реализовать функцию:
# def find_product(name):
# Требования:
# - функция принимает название товара
# - ищет товар в списке products
# - возвращает товар, если найден
# - возвращает None, если товар не найден
# Подсказки:
# - перебирай список через for
# - сравнивай product['name'] с name
# - используй return
# Добавить пункт меню:
# 4. Найти товар
# При выборе пункта:
# - запросить название товара
# - вызвать функцию find_product
# - вывести информацию о товаре или сообщение, что товар не найден

# ЧАСТЬ 2. Улучшить существующую функцию
# ЗАДАНИЕ 2. Улучшение функции show_products()
# Необходимо доработать функцию так, чтобы:
# - выводилось количество товара
# - выводилась общая стоимость товара (price * count)
# Пример вывода:
# 1. Хлеб — 150 ₸ (2 шт) = 300 ₸
# 2. Молоко — 400 ₸ (1 шт) = 400 ₸

# ЧАСТЬ 3. Дополнительно (по желанию)
# ЗАДАНИЕ 3. Улучшение поиска
# - поиск не должен зависеть от регистра
# - используйте метод lower()
# Условия сдачи
# - добавлена одна новая функция
# - улучшена одна существующая функция
# - программа запускается без ошибок
# - код читаемый и аккуратный


# mini project
# Это наша база
products = []
# Функция добавления товара
def add_product(name, price, quantity):
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    products.append(product)

# Функция вывода товара
def show_products():
    if len(products) == 0: 
        print("Товаров нет")
        return
    index = 1
    for product in products:
        print(index, ".", product["name"], "-", product["price"], product["quantity"], "тенге")
        index +=1

# Функция подсчета общей суммы
def get_total_price():
    total = 0
    for product in products:
        total+= product["price"]*product["quantity"]
    return total

# Реализовать функцию:
# def find_product(name):
# Требования:
# - функция принимает название товара
# - ищет товар в списке products
# - возвращает товар, если найден
# - возвращает None, если товар не найден
# Подсказки:
# - перебирай список через for
# - сравнивай product['name'] с name
# - используй return
# Добавить пункт меню:
# 4. Найти товар
# При выборе пункта:
# - запросить название товара
# - вызвать функцию find_product
# - вывести информацию о товаре или сообщение, что товар не найден    

def find_product(name):
    for product in products:
        if product["name"].lower() == name.lower():
            return product
    return None


# Функция меню
def show_menu():
    print("1. Добавить товар")
    print("2. Показать товары")
    print("3. Показать общую сумму")
    print("4. Найти товар")
    print("0. Выход")

while True:
    show_menu()
    choice = input("Выберете действие: ")
    if choice == "1":
        name = input("Название товара: ")
        price = int(input("Цена товара: "))
        quantity = int(input("Количество товара: "))
        add_product(name, price, quantity)
    elif choice =="2":
        show_products()
    elif choice =="3":
        total = get_total_price()
        print("Общая сумма:", total, "тенге")
    elif choice == "4":
        name = input("Введите название товара для поиска: ")
        product = find_product(name)
        if product:
            print("Товар найден:", product)
        else:
            print("Товар не найден")
    elif choice == "0":
        print("Выход из системы")
        break
    else:
        print("Неверный выбор")
