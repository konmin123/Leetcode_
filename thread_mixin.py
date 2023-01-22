"""class Parser:
    def send_request(self):
        print("Отправляю запрос...")
        time.sleep(1)

    def pars_request(self):
        print("Парсю результат...")
        time.sleep(0.75)

avito = Parser()
avito.send_request()
avito.pars_request()

Выполняется две секунды


Пример с миксином:
class Parser(ThreadMixin):
    def send_request(self):
        print("Отправляю запрос...")
        time.sleep(1)

    def pars_request(self):
        print("Парсю результат...")
        time.sleep(0.75)

avito = Parser()
avito.send_request()
avito.pars_request()

Выполняется 1 секунду
(Тк ThreadMixin добавляет всем методам класса многопоточность)"""
import threading
import time

from time import sleep


class ThreadMixin:
    def __init__(self):
        self.change_methods()

    @staticmethod
    def threading_method(method):
        th = threading.Thread(target=method)
        return th.start

    def change_methods(self):
        for index, str_method in enumerate(self.__dir__()[1::]):
            if str_method == '__doc__':
                break
            method = self.__getattribute__(str_method)
            self.__setattr__(str_method, self.threading_method(method))


class Parser(ThreadMixin):
    @staticmethod
    def send_request():
        print("Отправляю запрос...")
        sleep(1)
        print('выполнена send_request')

    @staticmethod
    def pars_request():
        print("Парсю результат...")
        sleep(0.75)
        print('выполнена pars_request')


avito = Parser()
start = time.time()
avito.send_request()
avito.pars_request()
end = time.time()
print(end - start)
