# 9. WAP to print all numbers in a range divisible by a given number.
start = int(input('Enter starting number: '))
end = int(input('Enter ending number: '))
n = int(input('Enter number: '))

for i in range(start, end + 1):
    if i % n == 0:
        print(i)