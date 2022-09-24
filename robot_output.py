"""given 2 minefield,
it is necessary to calculate the number of paths from the lower left corner to the upper right corner.
n is the width of the field,
m is the height of the field
input:  m = 5, n = 5
output: 70
constraint: m > 0, n > 0.
"""


def path_counter_1(n: int, m: int) -> int:  # первая версия (проблема в повторном рекурсивном вызове найденного эл-та)
    if m == 1 and n == 1:
        return 0
    elif m == 1 or n == 1:
        return 1
    else:
        return path_counter_1(n - 1, m) + path_counter_1(n, m - 1)


def step_one(n_: int, m_: int) -> int:  # вторая версия, проблема решена
    list_values = [[0 for _ in range(m_)] for _ in range(n_)]

    def path_counter(n: int, m: int) -> int:
        if n == 1 or m == 1:
            return 1
        elif n == 1 and m == 1:
            return 0
        elif list_values[n - 1][m - 1] != 0:
            return list_values[n - 1][m - 1]
        else:
            list_values[n - 1][m - 1] = path_counter(n - 1, m) + path_counter(n, m - 1)
            return list_values[n - 1][m - 1]
    return path_counter(n_, m_)


def my_idea(n: int, m: int) -> int:  # решение через последовательность
    list_values = [0 for i in range(m * n)]
    for i in range(n * m):
        if i == 0:
            list_values[i] = 0
        elif i < n:
            list_values[i] = 1
        elif i % n == 0:
            list_values[i] = 1
        else:
            list_values[i] = list_values[i - n] + list_values[i - 1]
    print(list_values)
    return list_values[n * m - 1]


if __name__ == '__main__':
    print(my_idea(5, 5))
