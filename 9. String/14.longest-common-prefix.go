/*
 * @lc app=leetcode id=14 lang=golang
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (43.00%)
 * Likes:    20257
 * Dislikes: 4833
 * Total Accepted:    5.1M
 * Total Submissions: 11M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 *
 * If there is no common prefix, return an empty string "".
 *
 *
 * Example 1:
 *
 *
 * Input: strs = ["flower","flow","flight"]
 * Output: "fl"
 *
 *
 * Example 2:
 *
 *
 * Input: strs = ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= strs.length <= 200
 * 0 <= strs[i].length <= 200
 * strs[i] consists of only lowercase English letters if it is non-empty.
 *
 *
 */

// @lc code=start
package main

import "slices"
func longestCommonPrefix(strs []string) string {
    slices.Sort(strs) // After sorting the most different two strings will be the first and the last
	first := strs[0]
	last := strs[len(strs) - 1]
	i := 0
	for ;i < min(len(first), len(last)); i++ {
		if first[i] != last[i] {
			break
		}
	}
	return first[:i]
}
// Time: O(N*log N + M)
// sorting + min(len(first), len(last))
// @lc code=end
