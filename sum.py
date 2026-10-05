def sum():
    m = int(input())
    s = input()
    n = int(input())

    if s == '+':
        print(m + n)
    elif s == '-':
        print(m - n)
    elif s == '*':
        print(m * n)
    elif s == '/':
        try:
            print(m / n)
        except ZeroDivisionError:
            print('not valid number')
sum()
