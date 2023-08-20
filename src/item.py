import csv
import math

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity

        # pass
    @property
    def pr_name(self):
        return self.__name

    @pr_name.setter
    def pr_name(self, short_name):
        if len(self.__name) > 10:
            print('Длина наименования товара превышает 10 символов')
            short_name = self.__name[:10]
        return short_name

    @staticmethod
    def string_to_number(num):
        i_num = float(num)
        return math.floor(i_num)

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row['name'], row['price'], row['quantity'])
                cls(row['name'], row['price'], row['quantity'])


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return int(self.price * self.quantity)


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)


it1 = Item("Смартфон", 10000, 20)
it2 = Item("Ноутбук", 20000, 5)
Item.all.append(it1)
Item.all.append(it2)
