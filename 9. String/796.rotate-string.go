/*
 * @lc app=leetcode id=796 lang=golang
 *
 * [796] Rotate String
 *
 * https://leetcode.com/problems/rotate-string/description/
 *
 * algorithms
 * Easy (58.30%)
 * Likes:    4654
 * Dislikes: 397
 * Total Accepted:    711.4K
 * Total Submissions: 1.1M
 * Testcase Example:  '"abcde"\n"cdeab"'
 *
 * Given two strings s and goal, return true if and only if s can become goal
 * after some number of shifts on s.
 *
 * A shift on s consists of moving the leftmost character of s to the rightmost
 * position.
 *
 *
 * For example, if s = "abcde", then it will be "bcdea" after one shift.
 *
 *
 *
 * Example 1:
 * Input: s = "abcde", goal = "cdeab"
 * Output: true
 * Example 2:
 * Input: s = "abcde", goal = "abced"
 * Output: false
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length, goal.length <= 100
 * s and goal consist of lowercase English letters.
 *
 *
 */

// @lc code=start
package main

import "strings"

func rotateString(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}
	// return bruteForce(s, goal)
	return optimal(s, goal)
}

// If goal is a rotation of s, then goal will always appear as a substring of s + s.
func optimal(s, goal string) bool {
	s = s + s
	return strings.Contains(s, goal)
}
// Time Complexity: O(N), because checking for a substring in s + s is linear in time.
// Space Complexity: O(N) for the space needed to store the concatenated string s + s.

func bruteForce(s, goal string) bool {
	for i := 0; i < len(s); i++ {
		rotated := s[i:] + s[:i]
		if rotated == goal {
			return true
		}
	}
	return false
}
// Time Complexity: O(N^2) since generating N rotations and each comparison takes O(N) time.
// Space Complexity: O(N) for the space needed to store each rotated string.

// @lc code=end
