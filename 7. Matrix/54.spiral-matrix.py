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

        answer = []
        row, col = len(matrix), len(matrix[0])
        top = 0
        bottom = row - 1
        left = 0
        right = col - 1
        while top < bottom and left < right:
            for j in range(left, right + 1):
                answer.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1

            for j in range(right, left - 1, -1):
                answer.append(matrix[bottom][j])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                answer.append(matrix[i][left])
            left += 1
            
        for row in range(top, bottom+1):
            for col in range(left, right+1):
                answer.append(matrix[row][col])
        return answer

# Golang
# func spiralOrder(matrix [][]int) []int {
# 	top, bottom := 0, len(matrix)-1
# 	left, right := 0, len(matrix[0])-1
# 	var res []int

# 	for top < bottom && left < right {
# 		for i := left; i <= right; i++ {
# 			res = append(res, matrix[top][i])
# 		}
# 		top++

# 		for i := top; i <= bottom; i++ {
# 			res = append(res, matrix[i][right])
# 		}
# 		right--

# 		for i := right; i >= left; i-- {
# 			res = append(res, matrix[bottom][i])
# 		}
# 		bottom--

# 		for i := bottom; i >= top; i-- {
# 			res = append(res, matrix[i][left])
# 		}
# 		left++
# 	}
# 	for i := top; i <= bottom; i++ {
# 		for j := left; j <= right; j++ {
# 			res = append(res, matrix[i][j])
# 		}
# 	}
#     return res
# }
# @lc code=end
