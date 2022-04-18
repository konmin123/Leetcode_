def insertion_sort(sequence: list) -> list:
    for j in range(1, len(sequence)):
        key = sequence[j]
        i = j - 1
        while i > -1 and sequence[i] > key:
            sequence[i + 1] = sequence[i]
            i -= 1
        sequence[i + 1] = key
    return sequence


def revers_insertion_sort(sequence: list) -> list:
    for j in range(1, len(sequence),):
        key = sequence[j]
        i = j - 1
        while i > -1 and sequence[i] < key:
            sequence[i + 1] = sequence[i]
            i -= 1
        sequence[i + 1] = key
    return sequence


print(insertion_sort([2, 5, 6, 9, 1, 3]))
print(revers_insertion_sort([2, 5, 6, 9, 1, 3]))
