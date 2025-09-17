/*
 * @lc app=leetcode id=48 lang=golang
 *
 * [48] Rotate Image
 *
 * https://leetcode.com/problems/rotate-image/description/
 *
 * algorithms
 * Medium (74.68%)
 * Likes:    19184
 * Dislikes: 919
 * Total Accepted:    2.5M
 * Total Submissions: 3.2M
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * You are given an n x n 2D matrix representing an image, rotate the image by
 * 90 degrees (clockwise).
 *
 * You have to rotate the image in-place, which means you have to modify the
 * input 2D matrix directly. DO NOT allocate another 2D matrix and do the
 * rotation.
 *
 *
 * Example 1:
 *
 *
 * Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * Output: [[7,4,1],[8,5,2],[9,6,3]]
 *
 *
 * Example 2:
 *
 *
 * Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
 * Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 *
 *
 *
 * Constraints:
 *
 *
 * n == matrix.length == matrix[i].length
 * 1 <= n <= 20
 * -1000 <= matrix[i][j] <= 1000
 *
 *
 */

// @lc code=start
/*
Rotating by 90 clockwise = Reversing and Transposing
Rotating by 90 anti-clockwise = Transposing and Reversing
*/
func rotate(matrix [][]int)  {
    slices.Reverse(matrix)
    for i := 0; i < len(matrix) - 1; i++ {
        for j := i + 1; j < len(matrix); j++ {
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        }
    }
}
// @lc code=end
