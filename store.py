#Создаем класс Store
class Store():
    def __init__(self, name, address, items = {}):
        self.name = name
        self.address = address
        self.items = items

    #Добавление товара
    def add_item(self,item_name, item_price):
        self.items[item_name] = item_price
        print(f"Товар {item_name} добавлен в магазин '{self.name}'.")

    #Удаление товара
    def delete_item(self,item_name):
        del self.items[item_name]
        print(f"Товар {item_name} удален из магазина '{self.name}'.")

    #Получение цены
    def get_item_price(self,item_name):
        try:
            return self.items[item_name]
        except KeyError:
            return None

    #Обновление цены товара
    def update_item_price(self,item_name,new_price):
            if item_name in self.items.keys():
                self.items[item_name] = new_price
                print(f"Цена товара {item_name} обновлена")
            else:
                print(f"Товар {item_name} отсутствует магазине '{self.name}'")