def myrange(start, stop, step=1):
    if step == 0:
        raise ValueError('Step cannot be zero')

    if step > 0:
        while start < stop:
            yield start
            start = start + step

    else:
        while start > stop:
            yield start
            start = start + step


for i in myrange(1, 10, 2):
    print(i, end=' ')