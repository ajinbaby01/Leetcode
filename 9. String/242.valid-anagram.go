/*
 * @lc app=leetcode id=242 lang=golang
 *
 * [242] Valid Anagram
 *
 * https://leetcode.com/problems/valid-anagram/description/
 *
 * algorithms
 * Easy (64.70%)
 * Likes:    13688
 * Dislikes: 457
 * Total Accepted:    5.4M
 * Total Submissions: 8M
 * Testcase Example:  '"anagram"\n"nagaram"'
 *
 * Given two strings s and t, return true if t is an anagram of s, and false
 * otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "anagram", t = "nagaram"
 *
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: s = "rat", t = "car"
 *
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length, t.length <= 5 * 10^4
 * s and t consist of lowercase English letters.
 *
 *
 *
 * Follow up: What if the inputs contain Unicode characters? How would you
 * adapt your solution to such a case?
 *
 */

// @lc code=start
package main
func isAnagram(s string, t string) bool {
    pattern := [26]int{}
	for _, c := range s {
		pattern[c - 'a']++
	}

	for _, c := range t {
		pattern[c - 'a']--
	}

	for _, val := range pattern {
		if val != 0 {
			return false
		}
	}
	return true
}
// @lc code=end
