#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (51.62%)
# Likes:    11215
# Dislikes: 183
# Total Accepted:    838K
# Total Submissions: 1.6M
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
  # '5'
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
#
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
#
#
# Example 1:
#
#
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
#
#
# Example 2:
#
#
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9
#
#
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
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

        i = 0
        j = col - 1

        while i != row and j != -1:
            if matrix[i][j] == target:
                return True
            if target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False
        # Time: O(m + n), Space: O(1)


# @lc code=end
