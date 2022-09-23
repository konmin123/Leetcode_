"""You are given a list of daytime temperatures, return a list of the number of days to a warmer day.
example of input data: [15, 11, 10, 12, 9, 16, 17]
output: [5, 2, 1, 2, 1, 'n/a']"""

seq = [15, 11, 10, 12, 9, 16, 17]


def brutal_force(sequence: list) -> list:
    output = []
    for index, value_i in enumerate(sequence):
        count = 0
        for value in sequence[index+1:]:
            count += 1
            if value > value_i:
                output.append(count)
                break
        else:
            output.append('n/a')
    return output


print(brutal_force(seq))


