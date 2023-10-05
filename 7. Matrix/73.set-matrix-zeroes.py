#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (53.24%)
# Likes:    13138
# Dislikes: 655
# Total Accepted:    1.1M
# Total Submissions: 2.1M
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row
# and column to 0's.
#
# You must do it in place.
#
#
# Example 1:
#
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
#
# Example 2:
#
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
#
#
# Follow up:
#
#
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
#
#
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # record = set()
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             record.add('row ' + str(i))
        #             record.add('column ' + str(j))

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if ('row ' + str(i)) in record:
        #             matrix[i][j] = 0
        #         elif ('column ' + str(j)) in record:
        #             matrix[i][j] = 0
        # Time: O(mn), Space: O(m+n)

        first_row = False
        first_col = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_col = True
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        # Time: O(mn), Space: O(1)

# @lc code=end
