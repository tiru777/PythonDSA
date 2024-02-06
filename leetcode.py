from typing import List
# sum two numbers based on target
def sum_two(array, target):  # 13
    length = len(array)  # 5
    indexx = False
    for i in range(length):  # 0,1,2,3,4
        if not indexx:
            for j in range(i + 1, length):  # 0,1,2,3,4
                if array[i] + array[j] == target:  # 11+2
                    print(array[i], array[j], array[i] + array[j])
                    index = [i, j]
                    indexx = True
                    break

    return index


# print(sum_two([3, 2, 4], 6))
# print(sum_two([2, 7, 11, 15], 9))
# print(sum_two([3, 3], 6))

def palindrome(n: int) -> bool:
    if str(n)[::-1] == str(n):
        return True
    return False


# print(palindrome(121))
# print(palindrome(-121))
# print(palindrome(10))

def first_occurance(string: str, search: str):
    if search in string:
        return string.find(search)
    return -1


# print(first_occurance("leetcode","leeto"))


# sum digits without using any loops/recursion
class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) < 1:
            return num
        else:
            result = 1 + (num - 1) % 9
            return result


# ss = Solution()
# print(ss.addDigits(12345))
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = string.punctuation
        for i in st:
            if i in s:
                s = s.replace(i, "")
        ss = s.replace(" ", "").lower()
        return ss == ss[::-1]


# ss = Solution()
# print(ss.isPalindrome("A man, a plan, a canal: Panama"))
# print(ss.isPalindrome("race a car"))
# print(ss.isPalindrome(" "))


# happy number
class Solution:
    def isHappy(self, n: int) -> bool:
        # while n!=1 and len(str(n)) >1:
        #     n = sum(int(i)**2 for i in str(n))
        #
        # return n == 1
        #     # elif len(str(n)) > 1:
        #     #     return self.isHappy(n)
        #     # else:

        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            print(visited)
            n = sum(int(i) ** 2 for i in str(n))
            print(n)
        return n == 1


# ss = Solution()
# print(ss.isHappy(1111111))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if i in nums:
                return True
        return False

# sss=Solution()
# import datetime
# print(datetime.datetime.now())
# print(sss.containsDuplicate([1,2,3,4]))
# print(datetime.datetime.now())
x = 7
print(int(x**(1/2)))

