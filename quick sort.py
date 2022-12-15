def quicksort(alist, left, right):
    """Sorts the list from indexes start to end - 1 inclusive."""
    if right - left > 1:
        p = partition(alist, left, right)
        quicksort(alist, left, p)
        quicksort(alist, p + 1, right)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and alist[i] <= pivot:
            i += 1
        while i <= j and alist[j] >= pivot:
            j -= 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


if __name__ == '__main__':
    seq = [2, 8, 12, 0, 1]
    quicksort(seq, 0, len(seq))
    print(seq)

