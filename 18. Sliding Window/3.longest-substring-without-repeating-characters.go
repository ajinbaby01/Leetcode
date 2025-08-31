/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (34.91%)
 * Likes:    42924
 * Dislikes: 2098
 * Total Accepted:    8M
 * Total Submissions: 21.4M
 * Testcase Example:  '"abcabcbb"'
 *
 * Given a string s, find the length of the longest substring without duplicate
 * characters.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * Notice that the answer must be a substring, "pwke" is a subsequence and not
 * a substring.
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= s.length <= 5 * 10^4
 * s consists of English letters, digits, symbols and spaces.
 *
 *
 */

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	setx := make(map[byte]struct{})
	left, maxLen := 0, 0
	for right, v := range s {
		char := byte(v)
		// If duplicate is found, remove all seen characters from the set
		// until the current character is also removed.
		// Now the set will have characters from a different substring
		// starting from the character to right of the removed duplicate.
		for _, ok := setx[char]; ok; _, ok = setx[char]{
			delete(setx, s[left])
			left++
		}
		setx[char] = struct{}{}
		maxLen = max(maxLen, right-left+1)
	}
	return maxLen
}
// @lc code=end
