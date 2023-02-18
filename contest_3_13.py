"""В постфиксной записи (или обратной польской записи) операция записывается
после двух операндов. Например, сумма двух чисел A и B записывается как A B +.
Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * +
означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не
требует скобок и дополнительных соглашений о приоритете операторов для своего
чтения.

Формат ввода
В единственной строке записано выражение в постфиксной записи, содержащее цифры
и операции +, -, *. Цифры и операции разделяются пробелами. В конце строки
может быть произвольное количество пробелов.

Формат вывода
Необходимо вывести значение записанного выражения.
Пример
Ввод	          Вывод
8 9 + 1 7 - *     - 102"""


def add(first_number: int, second_number: int) -> int:
    return first_number + second_number


def subtract(first_number: int, second_number: int) -> int:
    return first_number - second_number


def multiply(first_number: int, second_number: int) -> int:
    return first_number * second_number


expression = (input()).split()
stack_ = []
dict_element = {'+': add, '-': subtract, '*': multiply}
for element in expression:
    if element.isdigit():
        stack_.append(int(element))
    else:
        second_number = stack_.pop()
        first_number = stack_.pop()
        stack_.append(dict_element[element](first_number, second_number))
print(stack_.pop())
