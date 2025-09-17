/*
 * @lc app=leetcode id=54 lang=golang
 *
 * [54] Spiral Matrix
 *
 * https://leetcode.com/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (49.84%)
 * Likes:    16397
 * Dislikes: 1465
 * Total Accepted:    2M
 * Total Submissions: 3.7M
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * Given an m x n matrix, return all elements of the matrix in spiral order.
 *
 *
 * Example 1:
 *
 *
 * Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * Output: [1,2,3,6,9,8,7,4,5]
 *
 *
 * Example 2:
 *
 *
 * Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 *
 *
 *
 * Constraints:
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 10
 * -100 <= matrix[i][j] <= 100
 *
 *
 */

// @lc code=start
func spiralOrder(matrix [][]int) []int {
	var spiral []int
	rows := len(matrix)
	cols := len(matrix[0])

	top, left := 0, 0
	bottom, right := rows-1, cols-1

	for top <= bottom && left <= right {
		for i := left; i <= right; i++ {
			spiral = append(spiral, matrix[top][i])
		}
		top++

		for i := top; i <= bottom; i++ {
			spiral = append(spiral, matrix[i][right])
		}
		right--

		// in the case of single row, (top == bottom)
		// the first loop from left to right would have traversed the single row and then top would become greater than bottom.
		// if this check is not added, we would traverse the same row but from right to left (matrix[top][i] == matrix[bottom][i])
		if top <= bottom {
			for i := right; i >= left; i-- {
				spiral = append(spiral, matrix[bottom][i])
			}
			bottom--
		}

		// in the case of single column, (left == right)
		// the second loop from top to bottom would have traversed the single column and then right would become lesser than left.
		// if this check is not added, we would traverse the same column but from bottom to top (matrix[i][right] == matrix[i][left])
		if left <= right {
			for i := bottom; i >= top; i-- {
				spiral = append(spiral, matrix[i][left])
			}
			left++
		}
	}

	return spiral
}

// @lc code=end
