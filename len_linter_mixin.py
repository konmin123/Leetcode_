"""Напиши миксин, который проверяет все методы и выводит ошибку, если длинна
строчки в методе более 79 символов. Миксин обязательно должен быть классом и
работать через наследование"""
import inspect


class LenLinterMixin:
    def __init_subclass__(cls, **kwargs):
        cls.chek_len_line()

    @classmethod
    def chek_len_line(cls):
        lines = inspect.getsourcelines(cls)[0]
        for line in lines:
            if len(line) > 79:
                raise SyntaxError(f'Строка:{line} содержит более 79 символов!')


class Test(LenLinterMixin):
    def __init__(self, atr_1, atr_2):
        self.atr_1 = atr_1
        self.atr_2 = atr_2

    def some_method(self):
        return f'Сумма атрибутов равна: {self.atr_1 + self.atr_2}'

    def some_bad_method(self):
        return f'Сумма атрибутов равна: {self.atr_1 + self.atr_2} это означает, что'


# s = Test(1, 2)
# s.chek_len_line()
