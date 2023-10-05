#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (49.16%)
# Likes:    14445
# Dislikes: 377
# Total Accepted:    1.5M
# Total Submissions: 3M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# You are given an m x n integer matrix matrix with the following two
# properties:
#
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Given an integer target, return true if target is in matrix or false
# otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        # Binary search on each row
        # for i in range(row):
        #     left, right = 0, col - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if target == matrix[i][mid]:
        #             return True
        #         if target < matrix[i][mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        # return False
        # m = row, n = col
        # Time: O(m*logn), Space: O(1)

        # Binary search after finding the correct row
        # for i in range(row):
        #     if matrix[i][0] <= target <= matrix[i][-1]:
        #         left, right = 0, col - 1
        #         while left <= right:
        #             mid = (left + right) // 2
        #             if target == matrix[i][mid]:
        #                 return True
        #             if target < matrix[i][mid]:
        #                 right = mid - 1
        #             else:
        #                 left = mid + 1
        # return False
        # Time: O(m + logn), Space: O(1)

        # Binary search for finding the correct row
        # Then, binary search for finding the element
        # left, right = 0, row - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if matrix[mid][0] <= target <= matrix[mid][-1]:
        #         break
        #     if target < matrix[mid][0]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # required_row = mid

        # left, right = 0, col - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if target == matrix[required_row][mid]:
        #         return True
        #     if target < matrix[required_row][mid]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return False
        # Time: O(logm + logn) = O(log(mn)), Space: O(1)
        # Uses two binary searches

        # Treat the 2D matrix as a sorted array
        # row*col might cause overflow
        # Here, 1 <= m, n <= 100, meaning no overflow
        # Clarify about the constraints in the interview
        left, right = 0, row*col - 1
        while left <= right:
            mid = (left + right) // 2
            i = mid // col
            j = (mid % col)
            if target == matrix[i][j]:
                return True
            if target < matrix[i][j]:
                right = mid - 1
            else:
                left = mid + 1
        return False
        # Time: O(log(mn)), Space: O(1)

# @lc code=end
