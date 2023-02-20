"""Научитесь пользоваться стандартной структурой данных deque для целых чисел.
Напишите программу, содержащую описание дека и моделирующую работу дека,
реализовав все указанные здесь методы. Программа считывает последовательность
команд и в зависимости от команды выполняет ту или иную операцию.
После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:

push_front n
Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.

push_back n
Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.

pop_front
Извлечь из дека первый элемент. Программа должна вывести его значение.

pop_back
Извлечь из дека последний элемент. Программа должна вывести его значение.

front
Узнать значение первого элемента (не удаляя его). Программа должна вывести его
значение.

back
Узнать значение последнего элемента (не удаляя его). Программа должна вывести
его значение.

size
Вывести количество элементов в деке.

clear
Очистить дек (удалить из него все элементы) и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Гарантируется, что количество элементов в деке в любой момент не превосходит
100. Перед исполнением операций pop_front, pop_back, front, back программа
должна проверять, содержится ли в деке хотя бы один элемент. Если во входных
данных встречается операция pop_front, pop_back, front, back, и при этом дек
пуст, то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления деком, по одной на строке.

Формат вывода
Требуется вывести протокол работы дека, по одному сообщению на строке

Пример 1
Ввод	        Вывод
push_back 1     ok
back            1
exit            bye

Пример 2
Ввод	        Вывод
size            0
push_back 1     ok
size            1
push_back 2     ok
size            2
push_front 3    ok
size            3
exit            bye

Пример 3
Ввод	        Вывод
push_back 3     ok
push_front 14   ok
size            2
clear           ok
push_front 1    ok
back            1
push_back 2     ok
front           1
pop_back        2
size            1
pop_front       1
size            0
exit            bye"""
from collections import deque

deq = deque()


def push_front(value):
    deq.appendleft(value)
    print('ok')


def push_back(value):
    deq.append(value)
    print('ok')


def pop_front():
    if deq:
        print(deq.popleft())
    else:
        print('error')


def pop_back():
    if deq:
        print(deq.pop())
    else:
        print('error')


def front():
    if deq:
        print(deq[0])
    else:
        print('error')


def back():
    if deq:
        print(deq[-1])
    else:
        print('error')


def size():
    print(len(deq))


def clear():
    global deq
    deq = deque()
    print('ok')


command_dict = {
    'push_front': push_front,
    'push_back': push_back,
    'pop_front': pop_front,
    'pop_back': pop_back,
    'front': front,
    'back': back,
    'size': size,
    'clear': clear,
}
while True:
    command = input()
    if command == 'exit':
        print('bye')
        break
    elif command[-1].isdigit():
        command, arg = command.split()
        command_dict[command](int(arg))
    else:
        command_dict[command]()
