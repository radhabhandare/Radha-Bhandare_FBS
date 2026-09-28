for i in range(1, 6):

    print(1, end=' ')

    if i != 1 and i != 5:

        for j in range(1, i):
            print('  ', end='')

        print(i, end=' ')

    if i == 5:

        for j in range(2, 6):
            print(j, end='  ')

    print()