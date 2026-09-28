for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=' ')

    for j in range(1, 10 - 2 * i):
        print(' ', end=' ')

    for j in range(i, 0, -1):

        if i != 5 or j != 5:
            print(j, end=' ')

    print()