"""В этой задаче вам необходимо самостоятельно (не используя соответствующие
классы и функции стандартной библиотеки) организовать структуру данных Heap для
хранения целых чисел, над которой определены следующие операции: a) Insert(k) –
добавить в Heap число k ; b) Extract достать из Heap наибольшее число
(удалив его при этом).

Формат ввода
В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют
N команд, каждая в своей строке. Команда может иметь формат: “0 <число>” или
“1”, обозначающий, соответственно, операции Insert(<число>) и Extract.
Гарантируется, что при выполенении команды Extract в структуре находится по
крайней мере один элемент.

Формат вывода
Для каждой команды извлечения необходимо отдельной строкой вывести число,
полученное при выполнении команды Extract.

Пример 1
Ввод	    Вывод
2
0 10000
1           10000

Пример 2
Ввод	        Вывод
14
0 1
0 345
1               345
0 4346
1               4346
0 2435
1               2435
0 235
0 5
0 365
1               365
1               235
1               5
1               1"""


heap = []


def insert(value):
    heap.append(value)
    cur = len(heap) - 1
    while cur > 0 and heap[cur] > heap[(cur - 1)//2]:
        heap[cur], heap[(cur - 1)//2] = heap[(cur - 1)//2], heap[cur]
        cur = (cur - 1) // 2


def extract():
    out = heap[0]
    heap[0] = heap[-1]
    cur = 0
    while cur * 2 + 2 < len(heap):
        min_son_index = cur * 2 + 1
        if heap[cur * 2 + 2] > heap[min_son_index]:
            min_son_index = cur * 2 + 2
        if heap[cur] < heap[min_son_index]:
            heap[cur], heap[min_son_index] = heap[min_son_index], heap[cur]
            cur = min_son_index
        else:
            break
    heap.pop()
    return out


command_dict = {
    '0': insert,
    '1': extract,
}

f = input()
for _ in range(int(f)):
    command = input()
    if len(command) > 1:
        command, arg = command.split()
        command_dict[command](int(arg))
    else:
        print(command_dict[command]())