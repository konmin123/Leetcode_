def bubble_sort(seq: list) -> list:
    for position in range(len(seq) - 1):
        for index in range(len(seq) - position - 1):
            if seq[index] > seq[index + 1]:
                seq[index], seq[index + 1] = seq[index + 1], seq[index]
                print(seq)
    return seq


if __name__ == '__main__':
    print(bubble_sort([9, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    