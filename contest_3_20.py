"""Отсортируйте данный массив. Используйте пирамидальную сортировку.

Формат ввода
Первая строка входных данных содержит количество элементов в массиве N,
N ≤ 105. Далее задаются N целых чисел, не превосходящих по абсолютной величине
109.

Формат вывода
Выведите эти числа в порядке неубывания.

Пример 1
Ввод	Вывод
1
1        1

Пример 2
Ввод	Вывод
2
3 1      1 3 """
from collections import deque

heap = []
deq = deque()


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
second = input().split()
for value in second:
    insert(int(value))
for _ in range(int(f)):
    deq.appendleft(str(extract()))
print(' '.join(deq))
