/*
 * @lc app=leetcode id=557 lang=golang
 *
 * [557] Reverse Words in a String III
 *
 * https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
 *
 * algorithms
 * Easy (83.11%)
 * Likes:    6140
 * Dislikes: 253
 * Total Accepted:    1.1M
 * Total Submissions: 1.3M
 * Testcase Example:  `"Let's take LeetCode contest"`
 *
 * Given a string s, reverse the order of characters in each word within a
 * sentence while still preserving whitespace and initial word order.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "Let's take LeetCode contest"
 * Output: "s'teL ekat edoCteeL tsetnoc"
 *
 *
 * Example 2:
 *
 *
 * Input: s = "Mr Ding"
 * Output: "rM gniD"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * s contains printable ASCII characters.
 * s does not contain any leading or trailing spaces.
 * There is at least one word in s.
 * All the words in s are separated by a single space.
 *
 *
 */

// @lc code=start
package main

import "strings"

func reverseWords(s string) string {
	// words := strings.Fields(s)
	// for i, w := range words {
	// 	words[i] = reverse(w)
	// }
	// return strings.Join(words, " ")
	var sb strings.Builder
	for i := 0; i < len(s); {
		start := i
		for i < len(s) && s[i] != ' ' {
			i++
		}

		word := s[start:i]
		i++
		sb.WriteString(reverse(word))
		if i < len(s) {
			sb.WriteByte(' ')
		}
	}
	return sb.String()
}

func reverse(s string) string {
	b := []byte(s)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}

// @lc code=end
