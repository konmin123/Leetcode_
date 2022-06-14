class Purse:
    """Класс описывающий кошелёк"""
    def __init__(self, valuta, name="Unknown"):
        if valuta not in ('USD', 'EUR'):
            raise ValueError('Допустимые валюты: EUR и USD')
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, how_many):
        if isinstance(how_many, int) and how_many > 0:
            self.__money += how_many
        else:
            print("Введите корректное значение пополнения")

    def top_down_balance(self, how_many):
        if isinstance(how_many, int) and how_many > 0:
            if self.__money - how_many >= 0:
                self.__money -= how_many
            else:
                print("На вашем счету недостаточно средств")
        else:
            print("Введите корректное значение списания")

    def send_money(self, obj_for_up_balance, how_many):
        if isinstance(how_many, int) and how_many > 0:
            if self.__money - how_many >= 0:
                self.__money -= how_many
                Purse.top_up_balance(obj_for_up_balance, how_many)
            else:
                print("На вашем счету недостаточно средств")
        else:
            print("Введите корректное значение списания")

    def info(self):
        print(f"{self.__money} {self.valuta}")

    def __del__(self):
        print('Кошелёк удалён')


x = Purse("USD", "Ivan")
y = Purse("USD")
x.top_up_balance(100)
x.info()
y.info()
x.send_money(y, 100)
x.info()
y.info()