/*
 * @lc app=leetcode id=5 lang=golang
 *
 * [5] Longest Palindromic Substring
 *
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (33.97%)
 * Likes:    31356
 * Dislikes: 1931
 * Total Accepted:    4.1M
 * Total Submissions: 11.3M
 * Testcase Example:  '"babad"'
 *
 * Given a string s, return the longest palindromic substring in s.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "babad"
 * Output: "bab"
 * Explanation: "aba" is also a valid answer.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "cbbd"
 * Output: "bb"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 1000
 * s consist of only digits and English letters.
 *
 *
 */

// @lc code=start
func longestPalindrome(s string) string {
	// return firstSolution(s)
	return improvedSolution(s)
}

func improvedSolution(s string) string {
	n := len(s)
	if n < 2 {
		return s
	}
	start, maxLen := 0, 1

	for i := 0; i < n; {
		left, right := i, i
		for right+1 < n && s[right] == s[right+1] {
			right++
		}
		i = right + 1

		for left-1 >= 0 && right+1 < n && s[left-1] == s[right+1] {
			left--
			right++
		}

		if right-left+1 > maxLen {
			start = left
			maxLen = right - left + 1
		}
	}
	return s[start : start+maxLen]
}

func firstSolution(s string) string {
	left, right := 0, 0
	for idx, _ := range s {
		i, j := idx, idx
		for i >= 0 && j < len(s) && s[i] == s[j] {
			i--
			j++
		}
		j--
		i++
		if right-left < j-i {
			right, left = j, i
		}

		i, j = idx, idx+1
		for i >= 0 && j < len(s) && s[i] == s[j] {
			i--
			j++
		}
		j--
		i++
		if right-left < j-i {
			right, left = j, i
		}
	}
	return s[left : right+1]
}

// @lc code=end
