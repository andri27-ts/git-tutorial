def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == '__main__':
    a = 2
    b = 3
    print(f'{a} * {b} == {multiply(a, b)}')
    print(f'{a} / {b} == {divide(a, b)}')