"""
Recursion is best suited for any reverse of data like reverse string,reverse list,tuple
"""


# factorial
def fact(n: int) -> int:
    """
    Factorial by recursion: recursion will use stack data structure
    stack follows Last In first out
     Ex:n=5
     - 5*fact(4)=it will store in stack first=>5*24==>120
     - 4*fact(3)=it will store in stack second=>4*6=24
     - 3*fact(2)=it will store in stack third=>3*2=6
     - 2*fact(1)=it will store in stack fourth=>2*1=2
     - 1*fact(0)=it will store in stack last=Last InFirst out=>>1
    """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# print numbers between 1 to n
def natural_n(n):
    if n <= 0:
        return
    natural_n(n - 1)  # here function values stores in stack later it will take LIFO
    print(n)  # it will print values after closing of the function,
    # then values will take from stack


# sum of digits==>121
def func_sum(n):
    if n < 10:
        return n
    return n % 10 + func_sum(n // 10)


# sum of n natural numbers
def sum_n(n):
    if n <= 0:
        return 0
    else:
        return n + sum_n(n - 1)


# print(sum_n(5))  # 5,4,3,2,1,0 ==>


# palindrome
def palindrome(strr, start, end):
    if start >= end:
        return True
    return strr[start] == strr[end] and palindrome(strr, start + 1, end - 1)
    #


# print(palindrome("reer", 0, 3))

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
    # 2 * power(2,3)==>2*8=16
    # 2 * power(2,2)==>2*4=8
    # 2 * power(2,1)==>2*2=4
    # 2* power(2,0) ==>2*1=2


# print(power(2,4))

def prime_check(n, i):
    """ n==>
        4==1,2,3,4
        if only two factorial it is prime check
    """
    if i == 1:
        return True
    elif n % i == 0:
        return False
    return prime_check(n, i - 1)
    # prime(7,1)


n = 7


# print(prime_check(n,n//2))

def fabi_sequence(n):
    if n == 0 or n == 1:
        return n
    return fabi_sequence(n - 1) + fabi_sequence(n + 1)
    # many recursions
    # instead of recursion normal way good for fabinoci sequence
    #


def reverse_string(s):
    if len(s) == 1 or len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]


print(reverse_string("reddy"))
# instead of recursion normal way good for reverse

"""
# permutation
n = n!
"""
"""
Subset of the given string
n = 2^n
"""

