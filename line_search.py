def line_search(value_for_find, sequence):
    for index, value in enumerate(sequence):
        if value == value_for_find:
            return index
    return 'NIL'


print(line_search(6, [1, 2, 3, 4, 5, 6, 7]))

