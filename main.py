from store import *

#Создание магазинов
store1 = Store("Первый магазин", "Казань")
store2 = Store("Второй магазин", "Москва")
store3 = Store("Третий магазин", "Владимир")

#Добавление товаров в магазины
store1.add_item("бананы", 100)
store1.add_item("апельсины", 200)
store1.add_item("мандарины", 300)

store2.add_item("iphone 16", 150000)
store2.add_item("iphone 15", 100000)
store2.add_item("iphone 14", 80000)

store3.add_item("Лыжи", 10000)
store3.add_item("Санки", 1000)
store3.add_item("Сноуборд", 30000)

#Тест функций на примере третьего магазина
print("\nТЕСТИРОВАНИЕ ФУНКЦИЙ")
price = store3.get_item_price("Лыжи")                       #Получение цены товара
print(f"Цена товара 'Лыжи': {price}")
store3.update_item_price("Лыжи", 15000)  #Изменение цены товара
price = store3.get_item_price("Лыжи")                       #Получение новой цены товара
print(f"Цена товара 'Лыжи': {price}")
store3.delete_item("Санки")                                 #Удаление товара
store3.update_item_price("Санки", 2000)  #Попытка изменения цены удаленного товара
