import functools


def fibonacci2print(n: int):
    """print a fibonacci series up to n

    Args:
        n (_type_): _description_
    """
    if n <= 1:
        print(n)
    else:
        a, b = 0, 1
        while a < n:
            print(a, end=',')
            a, b = b, a + b
        print()


def fibonacci2list(n: int) -> list:
    """return a list of fibonacci series up to n

    Args:
        n (_type_): _description_
    """
    result = []

    if n <= 1:
        result.append(n)
    else:
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b

    return result


@functools.lru_cache
def fibonacci2value(n: int):
    if n <= 1:
        return n
    return fibonacci2value(n - 1) + fibonacci2value(n - 2)


if __name__ == '__main__':
    while True:
        try:
            input_n = int(input("------------pls enter an integer------------>>>"))
            fibonacci2print(input_n)
            print(fibonacci2list(input_n))
        except ValueError:
            print("Oops!  That was no valid integer number.  Try again...")
