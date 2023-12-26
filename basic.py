import math

"""
WPP to read a string and convert all even indexed values into upper case
"""


def even_index_upper(s: str):
    data = ""
    for index, i in enumerate(s):
        if index % 2 == 0:
            data = data + i.upper()
        else:
            data = data + i
    # for i in range(len(s)):
    #     if i % 2 == 0:
    #         data = data + s[i].upper()
    #     else:
    #         data = data + s[i]
    return data


# print(even_index_upper("thirumala reddy"))

# write a program to find max of two numbers and sorting

def sorting_list(l):
    for i in range(len(l)):  # 4
        for j in range(i + 1, len(l)):  # 2,4
            if l[i] > l[j]:  # 20>17
                l[i], l[j] = l[j], l[i]  # 17,20
    return l


l_d = [10, 20, 11, 17, 29]
data_sort = sorting_list(l_d)  # asc


# print("maximum of list:", data_sort[-1])
# print("ASC order of list:", data_sort)


def func_complexity(n: int) -> int:
    """

    :param n: number
    :return: how much time complexity(iterations)
    """
    c = 0
    i = 0
    while i < n:
        c = c + 1
        i = i + 1
    return c


# print("N=100 complexity is O(n):", func_complexity(100))


def func_complexity1(n: int) -> int:
    """

    :param n: number
    :return: how much time complexity(iterations) here two loops means approx is O(n^2)
    """
    c = 0
    for i in range(n):
        for j in range(n):
            c = c + 1
    return c


# print("N=100 complexity is O(n^2):", func_complexity1(100))


# factorial
"""
Algorithm
fact 5 ==> 5 x 4 x 3 x 2 x 1

"""


def factorial_m1(n):
    if n == 0:
        return 1
    else:
        fac = 1
        for i in range(1, n + 1):
            fac = fac * i
        return fac


def factorial_m2(n):
    return math.factorial(n)


def factorial_m3(n):
    # recursive function
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_m3(n - 1)
    # 5 * fact(4)
    # 5 * 4 * fact(3)
    # 5 * 4 * 3 * fact(2)
    # 5 * 4 * 3 * 2 * fact(1)
    # 5 * 4 * 3 * 2 * 1


# print(factorial_m1(5))
# print(factorial_m2(5))
# print(factorial_m3(5))

# given number prime or not
def prime_check(n):  # 5
    for i in range(2, n):  # 01234
        if n % i == 0:
            return False
    return True


# print(prime_check(31))


# n prime numbers
def n_prime(n):
    l = [i for i in range(1, n + 1) if prime_check(i)]
    # for i in range(1,n + 1):
    #     if prime_check(i):
    #         l.append(i)
    return l


# print(n_prime(7))
def prime_check2(n):  # 5
    """
    if n is divisible by factors of n is equal to 2 then it is prime
    Ex: 5
    fact of 5: 1 x 2 x 3 x 4 x 5
    - 5 % 1 ==0   - 5 % 4 !=0
    - 5 % 2 !=0   - 5 % 5 ==0
    - 5 % 3 !=0

    Here divisible by is two numbers [1,5] length must be two
    """
    factors = 0
    for i in range(1, n + 1):  # 01234
        if n % i == 0:
            factors = factors + 1
    return True if factors == 2 else False


def isprime_rec(n, i):
    if i == 1:
        return True
    elif n % i == 0:
        return False
    else:
        i = i - 1
        return isprime_rec(n, i)


n = 5
print(isprime_rec(n, n // 2))  # divising middle of value
