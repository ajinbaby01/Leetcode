/*
 * @lc app=leetcode id=1781 lang=golang
 *
 * [1781] Sum of Beauty of All Substrings
 *
 * https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/
 *
 * algorithms
 * Medium (65.41%)
 * Likes:    1486
 * Dislikes: 218
 * Total Accepted:    153.7K
 * Total Submissions: 211.3K
 * Testcase Example:  '"aabcb"'
 *
 * The beauty of a string is the difference in frequencies between the most
 * frequent and least frequent characters.
 *
 *
 * For example, the beauty of "abaacc" is 3 - 1 = 2.
 *
 *
 * Given a string s, return the sum of beauty of all of its substrings.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "aabcb"
 * Output: 5
 * Explanation: The substrings with non-zero beauty are
 * ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
 *
 * Example 2:
 *
 *
 * Input: s = "aabcbaa"
 * Output: 17
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <=^ 500
 * s consists of only lowercase English letters.
 *
 *
 */

// @lc code=start
package main

import "math"

func beautySum(s string) int {
	beautySum := 0
	for i := 0; i < len(s); i++ {
		freq := [26]int{}
		for j := i; j < len(s); j++ {
			freq[s[j]-'a']++
			minFreq, maxFreq := math.MaxInt, 0
			for _, count := range freq {
				if count > 0 {
					minFreq = min(minFreq, count)
					maxFreq = max(maxFreq, count)
				}
			}
			beautySum += (maxFreq - minFreq)
		}
	}
	return beautySum
}

// @lc code=end
