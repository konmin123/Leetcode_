"""Лайнландия представляет из себя одномерный мир, являющийся прямой, на
котором распологаются N городов, последовательно пронумерованных от 0 до N - 1.
Направление в сторону от первого города к нулевому названо западным, а в
обратную — восточным. Когда в Лайнландии неожиданно начался кризис, все были
жители мира стали испытывать глубокое смятение. По всей Лайнландии стали ходить
слухи, что на востоке живётся лучше, чем на западе. Так и началось Великое
Лайнландское переселение. Обитатели мира целыми городами отправились на восток,
покинув родные улицы, и двигались до тех пор, пока не приходили в город, в
котором средняя цена проживания была меньше, чем в родном.

Формат ввода
В первой строке дано одно число N (2≤N≤105) —
количество городов в Лайнландии. Во второй строке дано N чисел
ai(0≤ai≤109) — средняя цена проживания в городах с нулевого по (N - 1)-ый
соответственно.
Формат вывода
Для каждого города в порядке с нулевого по (N - 1)-ый выведите номер города, в
который переселятся его изначальные жители. Если жители города не остановятся
в каком-либо другом городе, отправившись в Восточное Бесконечное Ничто,
выведите -1 .

Пример
Ввод	                   Вывод
10
1 2 3 2 1 4 2 5 3 1        -1 4 3 4 -1 6 9 8 9 -1"""


def relocation(seq: list) -> str:
    stack: list = []
    for index, value in enumerate(seq):
        if stack:
            while stack and (stack[-1][1] > int(value)):
                elem = stack.pop()
                seq[elem[0]] = index
        stack.append((index, int(value)))
    for item in stack:
        seq[item[0]] = -1
    out: list = [str(x) for x in seq]
    return ' '.join(out)


first = input()
second = input().split()
print(relocation(second))