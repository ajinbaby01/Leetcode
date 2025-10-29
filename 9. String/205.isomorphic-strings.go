/*
 * @lc app=leetcode id=205 lang=golang
 *
 * [205] Isomorphic Strings
 *
 * https://leetcode.com/problems/isomorphic-strings/description/
 *
 * algorithms
 * Easy (43.45%)
 * Likes:    8851
 * Dislikes: 2052
 * Total Accepted:    1.3M
 * Total Submissions: 2.9M
 * Testcase Example:  '"egg"\n"add"'
 *
 * Given two strings s and t, determine if they are isomorphic.
 *
 * Two strings s and t are isomorphic if the characters in s can be replaced to
 * get t.
 *
 * All occurrences of a character must be replaced with another character while
 * preserving the order of characters. No two characters may map to the same
 * character, but a character may map to itself.
 *
 *
 * Example 1:
 * Input: s = "egg", t = "add"
 * Output: true
 * Example 2:
 * Input: s = "foo", t = "bar"
 * Output: false
 * Example 3:
 * Input: s = "paper", t = "title"
 * Output: true
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * t.length == s.length
 * s and t consist of any valid ascii character.
 *
 *
 */

// @lc code=start
package main

func isIsomorphic(s string, t string) bool {
	mapST := make(map[byte]byte)
	mapTS := make(map[byte]byte)

	for i := 0; i < len(s); i++ {
		c1, c2 := s[i], t[i]

		value, ok := mapST[c1]
		if ok {
			if value != c2 {
				return false
			}
		} else {
			mapST[c1] = c2
		}

		value, ok = mapTS[c2]
		if ok {
			if value != c1 {
				return false
			}
		} else {
			mapTS[c2] = c1
		}
	}
	return true
}

// @lc code=end
