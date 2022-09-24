"""given 2 minefield,
it is necessary to calculate the number of paths from the lower left corner to the upper right corner.
n is the width of the field,
m is the height of the field
input:  m = 5, n = 5
output: 70
constraint: m > 0, n > 0.
"""

COUNT = 1


def path_counter(n: int, m: int) -> int:
    if m == 1 and n == 1:
        return 0
    elif m == 1 or n == 1:
        return 1

    else:
        return path_counter(n - 1, m) + path_counter(n, m - 1)


if __name__ == '__main__':
    print(path_counter(3, 3))
