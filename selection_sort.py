def selection_sort(sequence):
    for i in range(len(sequence) - 1):
        index_min_elem = i
        for j in range(i, len(sequence)):
            if sequence[index_min_elem] > sequence[j]:
                index_min_elem = j
        sequence[i], sequence[index_min_elem] = sequence[index_min_elem], sequence[i]
    return sequence


print(selection_sort([8, 9, 7, 6, 3, 2]))
