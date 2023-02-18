"""Научитесь пользоваться стандартной структурой данных queue для целых чисел.
Напишите программу, содержащую описание очереди и моделирующую работу очереди,
реализовав все указанные здесь методы. Программа считывает последовательность
команд и в зависимости от команды выполняет ту или иную операцию. После
выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:

push n
Добавить в очередь число n (значение n задается после команды).
Программа должна вывести ok.

pop
Удалить из очереди первый элемент. Программа должна вывести его значение.

front
Программа должна вывести значение первого элемента, не удаляя его из очереди.

size
Программа должна вывести количество элементов в очереди.

clear
Программа должна очистить очередь и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций front и pop программа должна проверять, содержится
ли в очереди хотя бы один элемент. Если во входных данных встречается операция
front или pop, и при этом очередь пуста, то программа должна вместо числового
значения вывести строку error.

Формат ввода
Вводятся команды управления очередью, по одной на строке

Формат вывода
Требуется вывести протокол работы очереди, по одному сообщению на строке

Пример 1
Ввод	Вывод
push 1   ok
front    1
exit     bye

Пример 2
Ввод	Вывод
size      0
push 1    ok
size      1
push 2    ok
size      2
push 3    ok
size      3
exit      bye

Пример 3
Ввод	Вывод
push 3    ok
push 14   ok
size      2
clear     ok
push 1    ok
front     1
push 2    ok
front     1
pop       1
size      1
pop       2
size      0
exit      bye"""
from collections import deque

"""Очередь с защитой от ошибок"""
queue_ = deque()


def push_(n: int):
    queue_.append(n)
    print('ok')


def pop_():
    if queue_:
        print(queue_.popleft())
    else:
        print('error')


def front_():
    if queue_:
        print(queue_[0])
    else:
        print('error')


def size_():
    print(len(queue_))


def clear_():
    global queue_
    queue_ = deque()
    print('ok')


command_queue = {
    'push': push_,
    'pop': pop_,
    'front': front_,
    'size': size_,
    'clear': clear_,
}

while True:
    command = input()
    if command == 'exit':
        print('bye')
        break
    elif command[-1].isdigit():
        command, arg = command.split()
        command_queue[command](int(arg))
    else:
        command_queue[command]()
