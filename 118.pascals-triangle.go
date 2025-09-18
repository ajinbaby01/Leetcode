/*
 * @lc app=leetcode id=118 lang=golang
 *
 * [118] Pascal's Triangle
 *
 * https://leetcode.com/problems/pascals-triangle/description/
 *
 * algorithms
 * Easy (74.53%)
 * Likes:    14463
 * Dislikes: 541
 * Total Accepted:    2.4M
 * Total Submissions: 3.1M
 * Testcase Example:  '5'
 *
 * Given an integer numRows, return the first numRows of Pascal's triangle.
 *
 * In Pascal's triangle, each number is the sum of the two numbers directly
 * above it as shown:
 *
 *
 * Example 1:
 * Input: numRows = 5
 * Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
 * Example 2:
 * Input: numRows = 1
 * Output: [[1]]
 *
 *
 * Constraints:
 *
 *
 * 1 <= numRows <= 30
 *
 *
 */

// @lc code=start
func generate(numRows int) [][]int {
    // return calculateFromPreviousRow(numRows)
    return combinations(numRows)
}

// Calculate using (r-1)C(c-1) (1-index)
func combinations(numRows int) [][]int {
    pascalTri := [][]int{
        []int{1},
    }
    rowCount := 1
    for rowCount < numRows {
        row := []int{1}
        prev := 1
        for col := 1; col <= rowCount; col++ {
			currentElement := prev * (rowCount - col + 1) / col
            row = append(row, currentElement)
            prev = currentElement
        }
        pascalTri = append(pascalTri, row)
		rowCount++
    }
    return pascalTri
}

func calculateFromPreviousRow(numRows int) [][]int {
    pascalTri := [][]int{
        []int{1},
    }
    rowCount := 1
    for rowCount < numRows {
        row := []int{1}
        for i := 1; i < rowCount; i++ {
			row = append(row, pascalTri[rowCount - 1][i] + pascalTri[rowCount - 1][i-1])
        }
        row = append(row, 1)
        pascalTri = append(pascalTri, row)
		rowCount++
    }
	return pascalTri
}
// @lc code=end
