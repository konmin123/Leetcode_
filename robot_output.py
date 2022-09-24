"""given 2 minefield,
it is necessary to calculate the number of paths from the lower left corner to the upper right corner.
n is the width of the field,
m is the height of the field
input:  m = 5, n = 5
output: 70
constraint: m > 0, n > 0.
"""


def step_one(n_: int, m_: int) -> int:
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


if __name__ == '__main__':
    print(step_one(4, 3))
