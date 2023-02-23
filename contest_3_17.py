"""В игре в пьяницу карточная колода раздается поровну двум игрокам. Далее они
вскрывают по одной верхней карте, и тот, чья карта старше, забирает себе обе
вскрытые карты, которые кладутся под низ его колоды. Тот, кто остается без карт
 – проигрывает. Для простоты будем считать, что все карты различны по номиналу,
а также, что самая младшая карта побеждает самую старшую карту
("шестерка берет туза"). Игрок, который забирает себе карты, сначала кладет
под низ своей колоды карту первого игрока, затем карту второго игрока
(то есть карта второго игрока оказывается внизу колоды). Напишите программу,
которая моделирует игру в пьяницу и определяет, кто выигрывает. В игре
участвует 10 карт, имеющих значения от 0 до 9, большая карта побеждает меньшую,
карта со значением 0 побеждает карту 9.

Формат ввода
Программа получает на вход две строки: первая строка содержит 5 чисел,
разделенных пробелами — номера карт первого игрока, вторая – аналогично 5 карт
второго игрока. Карты перечислены сверху вниз, то есть каждая строка начинается
с той карты, которая будет открыта первой.

Формат вывода
Программа должна определить, кто выигрывает при данной раздаче, и вывести слово
first или second, после чего вывести количество ходов, сделанных до выигрыша.
Если на протяжении 106 ходов игра не заканчивается, программа должна вывести
слово botva.

Пример 1
Ввод	        Вывод
1 3 5 7 9
2 4 6 8 0       second 5

Пример 2
Ввод	        Вывод
2 4 6 8 0
1 3 5 7 9       first 5

Пример 3
Ввод	        Вывод
1 7 3 9 4
5 8 0 2 6       second 23"""
from collections import deque


def drunk_game(seq_1: list, seq_2: list) -> str:
    f_queue = deque(seq_1)
    s_queue = deque(seq_2)
    count = 0
    while f_queue and s_queue:
        f_card = f_queue.popleft()
        s_card = s_queue.popleft()
        if f_card == '0' and s_card == '9':
            f_queue.append(f_card)
            f_queue.append(s_card)
        elif f_card == '9' and s_card == '0':
            s_queue.append(f_card)
            s_queue.append(s_card)
        elif int(f_card) > int(s_card):
            f_queue.append(f_card)
            f_queue.append(s_card)
        else:
            s_queue.append(f_card)
            s_queue.append(s_card)
        count += 1
    return f'first {count}' if f_queue else f'second {count}'


f = input().split()
s = input().split()
print(drunk_game(f, s))