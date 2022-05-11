def school_mult()-> int:
    x = input('X: ')
    x = int(x)
    y = input("Y: ")

    revers_y = [int(y) // (10**i) % 10 for i in range(len(y))]

    for_sum = [revers_y[i] * x * 10 ** i for i in range(len(revers_y))]
    print("Naive Solution")
    print(revers_y)
    print(for_sum)
    print(sum(for_sum))


school_mult()

