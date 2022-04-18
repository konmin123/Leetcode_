arr = [i for i in range(1, 101)]


def binary_search_iterative(sequence: list, target: int):
    left = 0
    right = len(sequence) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == sequence[mid]:
            return mid
        elif target < sequence[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return None


print(binary_search_iterative(arr, 100))


def binary_search_rek(sequence: list, target: int, left: int, right: int):
    if left > right:
        return None
    mid = (left + right) // 2
    if sequence[mid] == target:
        return mid
    elif sequence[mid] < target:
        return binary_search_rek(sequence, target, mid + 1, right)
    else:
        return binary_search_rek(sequence, target, left, mid - 1)


print(binary_search_rek(arr, 100, 0, len(arr) - 1))

