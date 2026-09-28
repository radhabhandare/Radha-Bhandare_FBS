for i in range(1, 6):

    for j in range(1, 6 - i):
        print(' ', end=' ')

    print(1, end=' ')

    if i != 1:

        for j in range(1, 2 * i - 2):
            print(' ', end=' ')

        if i != 5:
            print(i, end=' ')

    if i == 5:

        for j in range(2, 6):
            print(j, end=' ')

    print()