/*
 * @lc app=leetcode id=567 lang=golang
 *
 * [567] Permutation in String
 *
 * https://leetcode.com/problems/permutation-in-string/description/
 *
 * algorithms
 * Medium (44.44%)
 * Likes:    12538
 * Dislikes: 500
 * Total Accepted:    1.3M
 * Total Submissions: 2.7M
 * Testcase Example:  '"ab"\n"eidbaooo"'
 *
 * Given two strings s1 and s2, return true if s2 contains a permutation of s1,
 * or false otherwise.
 *
 * In other words, return true if one of s1's permutations is the substring of
 * s2.
 *
 *
 * Example 1:
 *
 *
 * Input: s1 = "ab", s2 = "eidbaooo"
 * Output: true
 * Explanation: s2 contains one permutation of s1 ("ba").
 *
 *
 * Example 2:
 *
 *
 * Input: s1 = "ab", s2 = "eidboaoo"
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s1.length, s2.length <= 10^4
 * s1 and s2 consist of lowercase English letters.
 *
 *
 */

// @lc code=start
func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}

	// return bruteForceSorting(s1, s2)
	return slidingWindow(s1, s2)
}

func slidingWindow(s1, s2 string) bool {
	h1 := make(map[string]int)
	h2 := make(map[string]int)

	for i := 0; i < len(s1); i++ {
		h1[string(s1[i])]++
		h2[string(s2[i])]++
	}

	left := 0
	right := len(s1) - 1
	for right < len(s2) {
		if compareMap(h1, h2) {
			return true
		}
		if right == len(s2) - 1 {
			// We are at the last window
			break
		}

		h2[string(s2[left])]--
		left++
		right++
		h2[string(s2[right])]++
	}
	return false
}

func compareMap(h1, h2 map[string]int) bool {
	for char, count := range h1 {
		if h2[char] != count {
			return false
		}
	}
	return true
}

func bruteForceSorting(s1, s2 string) bool {
	s1Sorted := []byte(s1)

	sort.Slice(s1Sorted, func(i int, j int) bool {
		return s1Sorted[i] > s1Sorted[j]
	})
	s1 = string(s1Sorted)

	for i := 0; i < len(s2); i++ {
		for j := i; j < len(s2); j++ {
			subStr := s2[i : j+1]
			subStrSorted := []byte(subStr)
			sort.Slice(subStrSorted, func(a, b int) bool {
				return subStrSorted[a] > subStrSorted[b]
			})
			if s1 == string(subStrSorted) {
				return true
			}
		}
	}
	return false
}
// Time: O(n^3logn)
// @lc code=end
