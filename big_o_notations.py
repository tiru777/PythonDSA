def func_complexity_O_n(n: int) -> int:
    """

    :param n: number
    :return: how much time complexity(iterations) O(n)
    """
    c = 0
    i = 0
    while i < n:
        c = c + 1
        i = i + 1
    return c


# print("N=100 complexity is big O(n):", func_complexity_O_n(100))

def func_complexity_O_n_loop(n: int) -> int:
    """

    :param n: number
    :return: how much time complexity(iterations) O(n)
    even in multiple loop we are making with big O(n)
    """
    c = 0
    i = 0
    j = 0
    while i < n:  # 0<5
        while j < n:  # 0<5,1<5,2<5,3<5,4<5
            c = c + 1  # 1,2,3,4,5
            j = j + 1  # 1,2,3,4,5
            i = i + 1
    return c


print("N=5 complexity is big O(n):", func_complexity_O_n_loop(5))


def func_complexity1(n: int) -> int:
    """

    :param n: number
    :return: how much time complexity(iterations)
    here two loops means approx is big O(n^2)
    """
    c = 0
    for i in range(n):
        for j in range(n):
            c = c + 1
    return c


# print("N=100 complexity big O n square is O(n^2):", func_complexity1(100))

def func_complexity_log_n(n: int) -> int:
    """

    :param n: number
    :return: how much time complexity(iterations) big O(log n)

    """
    c = 0
    i = 1
    while i < n:
        c = c + 1
        i = i * 2
    return c


# print("N=100 complexity is big O(log n):", func_complexity_log_n(100))


def func_complexity_O_2(n: int) -> int:
    """

    :param n: number
    :return: how much time complexity(iterations)
    here two loops means approx is big O(n^2) + O(n^2)
                                  ==> 2 O(n^2) ==>O(n^2)
    """
    c = 0
    for i in range(n):
        for j in range(n):
            c = c + 1

    c = 0
    for i in range(n):
        for j in range(n):
            c = c + 1
    return c


# print("N=100 complexity big O n square is O(n^2):", func_complexity_O_2(100))

# 8 th video
