import re


def to_camel_case(text):
    words = re.split('_|-', text)
    return words[0] + ''.join(word.title() for word in words[1:])


assert to_camel_case('any_kebab-snake_case') == 'anyKebabSnakeCase'


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


s1 = Singleton()
s2 = Singleton()

assert id(s1) == id(s2)


def count_bits(n: int) -> int:
    return bin(n).count('1')


assert count_bits(0) == 0
assert count_bits(4) == 1
assert count_bits(10) == 2


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


assert digital_root(9) == 9
assert digital_root(10) == 1
assert digital_root(19) == 1


def even_or_odd(number: int) -> str:
    return "Even" if number % 2 == 0 else "Odd"


assert even_or_odd(2) == "Even"
assert even_or_odd(3) == "Odd"
