/*
 * @lc app=leetcode id=424 lang=golang
 *
 * [424] Longest Repeating Character Replacement
 *
 * https://leetcode.com/problems/longest-repeating-character-replacement/description/
 *
 * algorithms
 * Medium (54.16%)
 * Likes:    12181
 * Dislikes: 683
 * Total Accepted:    1.2M
 * Total Submissions: 2.1M
 * Testcase Example:  '"ABAB"\n2'
 *
 * You are given a string s and an integer k. You can choose any character of
 * the string and change it to any other uppercase English character. You can
 * perform this operation at most k times.
 *
 * Return the length of the longest substring containing the same letter you
 * can get after performing the above operations.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "ABAB", k = 2
 * Output: 4
 * Explanation: Replace the two 'A's with two 'B's or vice versa.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "AABABBA", k = 1
 * Output: 4
 * Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
 * The substring "BBBB" has the longest repeating letters, which is 4.
 * There may exists other ways to achieve this answer too.
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s consists of only uppercase English letters.
 * 0 <= k <= s.length
 *
 *
 */

// @lc code=start
func characterReplacement(s string, k int) int {
	l, res, maxf := 0, 0, 0
	hashMap := make(map[byte]int)
	for r, c := range s {
		char := byte(c)
		hashMap[char]++
		windowLen := r - l + 1
		// maxf := findMaxFreq(hashMap)
		maxf = max(hashMap[char], maxf) // Time: O(n)
		if windowLen-maxf <= k {
			res = max(res, windowLen)
		} else {
			hashMap[byte(s[l])]--
			l++
		}
	}
	return res
}

// Find the max frequency in the current window
func findMaxFreq(hashMap map[byte]int) int {
	maxf := 0
	for _, v := range hashMap {
		maxf = max(maxf, v)
	}
	return maxf
}
// Time: O(26n)

// @lc code=end
