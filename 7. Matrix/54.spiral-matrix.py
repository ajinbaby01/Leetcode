# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (47.44%)
# Likes:    13486
# Dislikes: 1171
# Total Accepted:    1.2M
# Total Submissions: 2.5M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        while matrix:
            answer.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return answer

        # answer = []
        # row, col = len(matrix), len(matrix[0])
        # top = 0
        # bottom = row - 1
        # left = 0
        # right = col - 1
        # while top < bottom and left < right:
        #     for j in range(left, right + 1):
        #         answer.append(matrix[top][j])

        #     for i in range(top + 1, bottom + 1):
        #         answer.append(matrix[i][right])

        #     for j in range(right - 1, left - 1, -1):
        #         answer.append(matrix[bottom][j])

        #     for i in range(bottom - 1, top, -1):
        #         answer.append(matrix[i][left])

        #     left += 1
        #     right -= 1
        #     top += 1
        #     bottom -= 1
        # for row in range(top, bottom+1):
        #     for col in range(left, right+1):
        #         answer.append(matrix[row][col])
        # return answer

# @lc code=end
