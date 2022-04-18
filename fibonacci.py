def fibonacci(target: int):
    a = 0  # 1 число
    b = 1  # 2 число
    for i in range(target-2):
        a, b = b, a + b
    print(a+b)


fibonacci(8)


def din_forward_fibonacci(n):
    fib_numbers = [0] * n

    fib_numbers[0] = 0
    fib_numbers[1] = 1

    for i in range(2, n):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
        print(f"{i}-состояние", fib_numbers)
    print(fib_numbers[-1])


din_forward_fibonacci(9)


def din_revers_fibonacci(n):
    fib_numbers = [0] * n

    fib_numbers[0] = 0
    fib_numbers[1] = 1

    for i in range(2, n):
        if i+1 < n:
            fib_numbers[i+1] = fib_numbers[i] + fib_numbers[i+1]
        if i+2 < n:
            fib_numbers[i+2] += fib_numbers[i]
    print(fib_numbers[-1])


din_forward_fibonacci(9)