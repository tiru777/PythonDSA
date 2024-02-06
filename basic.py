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


def max_list(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max


# print(max_list([1,2,10,22,34]))


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
    # 5 * 4 * 3 * 2 * fact(0)


# print(factorial_m1(5))
# print(factorial_m2(0))
# print(factorial_m3(5))

# given number prime or not
def prime_check(n):  # 5
    for i in range(2, n):  # 01234
        if n % i == 0:
            return False
    return True


# print(prime_check(2))


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


# print(isprime_rec(n, n // 2))  # divising middle of value


# extract digits from number
def extract_digits(n):
    """
    Ex: 125 should extract 5, 2, 1 digits
    1 x 100 position = 100
    2 x 10  position =  20
    5 x 1   position =   5
    -------------------------
                     =  125
    ------------------------------
    """

    while n != 0:
        digit = n % 10
        n = n // 10
        print("digit is:", digit)  # 5 4 2


# extract_digits(245)


def extract_digits_m2(n):
    n = str(n)[::-1]
    for i in n:
        print(i)


# extract_digits_m2(2465)


# palindrome
def palindrome(data):
    # if str(data)[::-1] == str(data):
    #     return True
    return str(data)[::-1] == str(data)


# print(palindrome("aba"))
# print(palindrome(121))

"""
Sum of n natural numbers
Ex: 5 --> 0+1+2+3+4+5 ==15

Algorithm
-----------
Step 1: read the number
Step 2: Apply the logic
Step 3: return output
"""


def sum_natu(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum
    # M2: sum = sum(list(range(n+1)))
    # M3: n*(n+1)/2


def sum_natural_rec_m4(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural_rec_m4(n - 1)


# print(sum_natural_rec_m4(3))

# how many trailing zeros present in number
def trail_zero(n):
    data = str(n)[::-1]
    c = 0
    for i in data:
        if int(i) > 0:
            break
        if int(i) == 0:
            c = c + 1
    return c


# print(trail_zero(110))

def is_perfect_number(n):
    """
    Perfect number: factor of n sum is equal to n, excluding the n
    Ex:6
    factors or divisors= 1,2,3,6
    exclude n factor = sum = 1+2+3 = 6
    """
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    return sum == n


# print(is_perfect_number(28))


def is_armstrong_number(n):
    """

    123 ==> 1^3 +2^3 +3^3 = 1+8+27 ==>36
    36 is not equal to 123 so its not a armstrong number

    153 ==> 1^3+5^3+3^3 =1+125+27 ==>153
    153 = 153 so its armstrong number

    """
    sum = 0
    for i in str(n):
        sum = sum + int(i) ** 3
    return sum == n


# print(is_armstrong_number(370))

def is_strong_number(n):
    """
    123 = >1! +2! +3! =1+2+6 =9
    123 not equal to 9 so it is not strong number
    145 ==> 1! +4! +5! =1+24+120 =145
    145 equal to 145 is a strong number
    """
    sum = 0
    for i in str(n):
        sum = sum + factorial_m1(int(i))
    return sum == n


# print(is_strong_number(145))

def feb_sequence(n):
    """
    sum of two previous numbers is a new number
    First two numbers are constant == 0,1
    0,1,1,2,3,5
    """
    fb_seq = []
    a = 0
    b = 1
    fb_seq.append(a)
    fb_seq.append(b)
    for i in range(n - 2):
        c = a + b
        fb_seq.append(c)
        a = b
        b = c

    return fb_seq


def fab_yield(n):
    l = []  # 0,1,1,2
    for i in range(n):  # 0,1,2,3
        if i == 0 or i == 1:
            l.append(i)
        else:
            l.append(l[i - 1] + l[i - 2])  # 1+1,
    return l


def feb_sequence_m2(n):
    data = []
    for i in range(n):  # 0,1,2,3,4
        if i == 0 or i == 1:
            data.append(i)
        else:
            data.append(data[i - 2] + data[i - 1])
            # fetching previous value and before that
    return data


# # print(feb_sequence(8))
# print(feb_sequence_m2(0))
# print(fab_yield(0))  # 1, 1, 2, 4
# print(feb_sequence(0))


def treb_sequence(n):
    """
    sum of two previous numbers is a new number
    First two numbers are constant == 0,1,2
    0,1,2,3,6
    """
    data = []
    for i in range(n):  # 0,1,2,3,4
        if i == 0 or i == 1 or i == 2:
            data.append(i)
        else:
            data.append(data[i - 3] + data[i - 2] + data[i - 1])
            # fetching previous value and before that
    return data


# print(treb_sequence(5))  # [0, 1, 2, 3, 6]
# print(treb_sequence(6))  # [0, 1, 2, 3, 6, 11]

# How to swap first and last element present in list
"""
x = [1, 2, 3, 4, 5]
x[0], x[-1] = x[-1], x[0]
print(x)
"""


# To remove Duplicate elements present in list
def remove_duplicates(l):
    """
    if we use set it will not maintain order, it will change order
    """
    l1 = []
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1


# print(remove_duplicates([1,2,3,1,2,4,5,1,2,3]))


# left rotate ==> [1, 2, 3, 4, 5] ==[5, 2, 3, 4, 1]
l = [1, 2, 3, 4, 5]
# v1
"""
l = l[1:] + l[0:1]
print(l)
"""
'''
# v2
l.append(l.pop(0))
print(l)
'''


def left_rotate(l):
    n = len(l)
    x = l[0]
    for i in range(1, n):
        l[i - 1] = l[i]
    l[n - 1] = x
    return l


# print(left_rotate([1, 2, 3, 4, 5]))

# right rotate ==[1, 2, 3, 4, 5] == [5,1, 2, 3, 4]
"""
l = l[-1:] +l[0:len(l)-1]
print(l)
"""
"""
l.insert(0, l.pop())
print(l)
"""

# left rotate by "d" rotations
'''
lis = [1, 2, 3, 4, 5] # ==>[4, 5, 1, 2, 3]
d_r = 3
lis = lis[d_r:]+lis[:d_r]
print(lis)
'''

from collections import deque


def n_rotates_left(l, d):
    """ dq.rotate if - or + (negitive or positive)
        means left rotate those numbers"""
    dq = deque(l)
    dq.rotate(-d)  # negitive means left rotate
    return list(dq)


# print(n_rotates_left([1, 2, 3, 4, 5], 3))
def left_n_rotate(l, d):
    for i in range(0, d):
        l.append(l.pop(0))
    return l


# print(left_n_rotate([1, 2, 3, 4, 5],2))


# right rotate
def n_rotates_right(l, d):
    """ dq.rotate if - or + (negitive or positive)
        means right rotate those numbers"""
    dq = deque(l)
    dq.rotate(d)  # positive means right rotate
    return list(dq)

# print(n_rotates_right([1, 2, 3, 4, 5], 3))
