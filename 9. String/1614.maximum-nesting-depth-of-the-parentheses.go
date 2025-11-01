/*
 * @lc app=leetcode id=1614 lang=golang
 *
 * [1614] Maximum Nesting Depth of the Parentheses
 *
 * https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
 *
 * algorithms
 * Easy (83.74%)
 * Likes:    2734
 * Dislikes: 521
 * Total Accepted:    501.2K
 * Total Submissions: 592.7K
 * Testcase Example:  '"(1+(2*3)+((8)/4))+1"'
 *
 * Given a valid parentheses string s, return the nesting depth of s. The
 * nesting depth is the maximum number of nested parentheses.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "(1+(2*3)+((8)/4))+1"
 *
 * Output: 3
 *
 * Explanation:
 *
 * Digit 8 is inside of 3 nested parentheses in the string.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "(1)+((2))+(((3)))"
 *
 * Output: 3
 *
 * Explanation:
 *
 * Digit 3 is inside of 3 nested parentheses in the string.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "()(())((()()))"
 *
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 100
 * s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and
 * ')'.
 * It is guaranteed that parentheses expression s is a VPS.
 *
 *
 */

// @lc code=start
package main

func maxDepth(s string) int {
	depth := 0
	maxDepth := 0
	for _, c := range s {
		switch c {
		case '(':
			depth++
			maxDepth = max(maxDepth, depth)
		case ')':
			depth--
		}
	}
	return maxDepth
}

// @lc code=end
