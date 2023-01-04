"""Необходимо написать декоратор, который будет проверять тип ожидаемых и
передаваемых аргументов в функцию, и возвращать ошибку если они не совпадают.
Пример: функция get_sum принимает два аргумента, оба должны быть целыми числами
(int), если мы передадим два целых числа (int), то программа корректно
отработает. Если мы попробуем передать любой другой тип данных, то декоратор
вернёт ошибку, о не совпадении ожидаемых типов данных с пришедшими"""


def decorator(func):
    def wrapper(*args, **kwargs):
        arguments_values = list(args)
        arguments_types = list(func.__annotations__.values())
        for index in range(len(arguments_values)):
            element = arguments_values[index]
            type_ = arguments_types[index]
            if type(element) is not type_:
                raise TypeError
        for item in kwargs.items():
            type_kwarg = func.__annotations__[item[0]]
            if type(item[1]) is not type_kwarg:
                raise TypeError
        return func(*args, **kwargs)
    return wrapper


@decorator
def get_sum(first_number: int, second_number: int) -> int:
    return first_number + second_number


print(get_sum(2, second_number=2))
