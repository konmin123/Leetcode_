"""Имеется калькулятор, который выполняет следующие операции:

умножить число X на 2;
умножить число X на 3;
прибавить к числу X единицу.
Определите, какое наименьшее количество операций требуется, чтобы получить из
числа 1 число N.

Формат ввода
Во входном файле написано натуральное число N, не превосходящее 106.

Формат вывода
В первой строке выходного файла выведите минимальное количество операций.
Во второй строке выведите числа, последовательно получающиеся при выполнении
операций. Первое из них должно быть равно 1, а последнее N. Если решений
несколько, выведите любое.

Пример 1
Ввод	Вывод
1       0
        1

Пример 2
Ввод	Вывод
5       3
        1 3 4 5"""

a = float(input())

count = 0

while a != 1:

    if (a % 2 == 0 or a % 3 == 0):
        if (((a - 1) % 9 == 0) and a % 16 != 0):
            a = (a - 1)/9
            count += 3
        else:
            if ((a - 1) % 32 == 0):
                a = (a - 1)/32
                count += 6
            if (a % 16 == 0):
                a = a/16
                count += 4
            if (a % 16 != 0 and a % 2 == 0):
                a = a/2
                count += 1
            if (a % 9 == 0 or a % 3 == 0):
                a = a/3
                count += 1
    else:
        if a != 1:
            a = a - 1
            count += 1
        if a == 1:
            break
print(count)