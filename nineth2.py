def read_and_print():
    x = int(input())
    if x == 0:
        return

    y = int(input())
    print(x)

    if y == 0:
        return

    read_and_print()

read_and_print()
