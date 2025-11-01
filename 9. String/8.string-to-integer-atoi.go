/*
 * @lc app=leetcode id=8 lang=golang
 *
 * [8] String to Integer (atoi)
 *
 * https://leetcode.com/problems/string-to-integer-atoi/description/
 *
 * algorithms
 * Medium (17.38%)
 * Likes:    5837
 * Dislikes: 15214
 * Total Accepted:    2.2M
 * Total Submissions: 11M
 * Testcase Example:  '"42"'
 *
 * Implement the myAtoi(string s) function, which converts a string to a 32-bit
 * signed integer.
 *
 * The algorithm for myAtoi(string s) is as follows:
 *
 *
 * Whitespace: Ignore any leading whitespace (" ").
 * Signedness: Determine the sign by checking if the next character is '-' or
 * '+', assuming positivity if neither present.
 * Conversion: Read the integer by skipping leading zeros until a non-digit
 * character is encountered or the end of the string is reached. If no digits
 * were read, then the result is 0.
 * Rounding: If the integer is out of the 32-bit signed integer range [-2^31,
 * 2^31 - 1], then round the integer to remain in the range. Specifically,
 * integers less than -2^31 should be rounded to -2^31, and integers greater
 * than 2^31 - 1 should be rounded to 2^31 - 1.
 *
 *
 * Return the integer as the final result.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "42"
 *
 * Output: 42
 *
 * Explanation:
 *
 *
 * The underlined characters are what is read in and the caret is the current
 * reader position.
 * Step 1: "42" (no characters read because there is no leading whitespace)
 * ⁠        ^
 * Step 2: "42" (no characters read because there is neither a '-' nor '+')
 * ⁠        ^
 * Step 3: "42" ("42" is read in)
 * ⁠          ^
 *
 *
 *
 * Example 2:
 *
 *
 * Input: s = " -042"
 *
 * Output: -42
 *
 * Explanation:
 *
 *
 * Step 1: "   -042" (leading whitespace is read and ignored)
 * ⁠           ^
 * Step 2: "   -042" ('-' is read, so the result should be negative)
 * ⁠            ^
 * Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
 * ⁠              ^
 *
 *
 *
 * Example 3:
 *
 *
 * Input: s = "1337c0d3"
 *
 * Output: 1337
 *
 * Explanation:
 *
 *
 * Step 1: "1337c0d3" (no characters read because there is no leading
 * whitespace)
 * ⁠        ^
 * Step 2: "1337c0d3" (no characters read because there is neither a '-' nor
 * '+')
 * ⁠        ^
 * Step 3: "1337c0d3" ("1337" is read in; reading stops because the next
 * character is a non-digit)
 * ⁠            ^
 *
 *
 *
 * Example 4:
 *
 *
 * Input: s = "0-1"
 *
 * Output: 0
 *
 * Explanation:
 *
 *
 * Step 1: "0-1" (no characters read because there is no leading whitespace)
 * ⁠        ^
 * Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
 * ⁠        ^
 * Step 3: "0-1" ("0" is read in; reading stops because the next character is a
 * non-digit)
 * ⁠         ^
 *
 *
 *
 * Example 5:
 *
 *
 * Input: s = "words and 987"
 *
 * Output: 0
 *
 * Explanation:
 *
 * Reading stops at the first non-digit character 'w'.
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= s.length <= 200
 * s consists of English letters (lower-case and upper-case), digits (0-9), '
 * ', '+', '-', and '.'.
 *
 *
 */

// @lc code=start
package main

const (
	Int32Min = -1 << 31  // -2147483648
	Int32Max = 1<<31 - 1 // 2147483647
)

func myAtoi(s string) int {
	i, n := 0, len(s)
	integer := 0
	sign := 1

	for i < n && s[i] == ' ' {
		i++
	}

	if i == n {
		return 0
	}

	if s[i] == '-' {
		sign = -1
		i++
	} else if s[i] == '+' {
		i++
	}

	for i < len(s) && s[i] >= '0' && s[i] <= '9' {
		digit := int(s[i] - '0')

		/*
			Check overflow BEFORE multiplication and addition
			First part checks if multiplying integer by 10 would exceed Int32Max
			Second part handles the edge case where integer = 214748364 (exactly Int32Max/10). Here, the result depends on the digit being added:​
			If digit ≤ 7: 214748364 × 10 + 7 = 2147483647 (valid, equals Int32Max)
			If digit > 7: 214748364 × 10 + 8 = 2147483648 (overflow)
		*/
		if integer > Int32Max/10 || (integer == Int32Max/10 && digit > 7) {
			if sign < 0 {
				return Int32Min
			}
			return Int32Max
		}
		integer = integer*10 + digit
		i++
	}

	return sign * integer
}

// @lc code=end
