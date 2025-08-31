#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (66.19%)
# Likes:    4774
# Dislikes: 1930
# Total Accepted:    783.2K
# Total Submissions: 1.2M
# Testcase Example:  '38'
#
# Given an integer num, repeatedly add all its digits until the result has only
# one digit, and return it.
#
#
# Example 1:
#
#
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
#
#
# Example 2:
#
#
# Input: num = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= num <= 2^31 - 1
#
#
#
# Follow up: Could you do it without any loop/recursion in O(1) runtime?
#
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # return self.listComprehensionLoop(num)
        # return self.iterative(num)
        # return self.bigO1(num)
        return self.oneLiner(num)

    def listComprehensionLoop(self, num):
        num = str(num)
        while len(num) != 1:
            num = str(sum([int(i) for i in num]))
        return int(num)

    def iterative(self, num):
        # summed = 0
        # while (num > 9):
        #     while (num):
        #         summed += num % 10
        #         num //= 10
        #     num = summed
        #     summed = 0
        # return num

        summed = num
        while summed > 9:
            summed = 0
            while num:
                summed += num % 10
                num //= 10
            num = summed
        return summed

    def bigO1(self, num):
        # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        # https://leetcode.com/problems/add-digits/solutions/1754046/java-c-python-solution-with-math-s-explained/
        if num == 0:
            return 0

        if num % 9 == 0:
            return 9

        return num % 9

    def oneLiner(self, num):
        if num == 0:
            return num

        # Only below line required in C, C++, Java
        # Because (0 - 1) % 9 = -1 in above languages
        # In Python, -1 % 9 = 8, so num = 0 case fails
        return 1 + (num - 1) % 9


# @lc code=end
