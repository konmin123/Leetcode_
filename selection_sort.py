def selection_sort(sequence):
    for i in range(len(sequence) - 1):
        index_min = i
        print('i=', i)
        for j in range(i, len(sequence)):
            if sequence[i] > sequence[j]:
                index_min = j
        sequence[i], sequence[index_min] = sequence[index_min], sequence[i]
        print(sequence)
    return sequence


print(selection_sort([8, 9, 7, 6]))
