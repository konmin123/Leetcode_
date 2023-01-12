def decorator(func):
    def wrapper(*args, **kwargs):
        print('1')
        print('*args', args)
        print('**kwargs', kwargs)
        result = func(*args, **kwargs)
        print('завершение работы декоратора')
        return result
    return wrapper

@decorator
def func(*args, **kwargs):
    print('Результат внутри функции funk')
    return sum(args) + sum(kwargs.values())


print(f'Результат {func(1, 2, с=5, d=10)}')


# def is_prime(number: int) -> bool:
#     for divisor in range(2, (number//2)+1):
#         if number % divisor == 0:
#             return False
#     return True
#
#
# print(is_prime(1))
