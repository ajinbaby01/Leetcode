/*
 * @lc app=leetcode id=451 lang=golang
 *
 * [451] Sort Characters By Frequency
 *
 * https://leetcode.com/problems/sort-characters-by-frequency/description/
 *
 * algorithms
 * Medium (72.63%)
 * Likes:    8992
 * Dislikes: 327
 * Total Accepted:    1M
 * Total Submissions: 1.4M
 * Testcase Example:  '"tree"'
 *
 * Given a string s, sort it in decreasing order based on the frequency of the
 * characters. The frequency of a character is the number of times it appears
 * in the string.
 *
 * Return the sorted string. If there are multiple answers, return any of
 * them.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "tree"
 * Output: "eert"
 * Explanation: 'e' appears twice while 'r' and 't' both appear once.
 * So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
 * answer.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "cccaaa"
 * Output: "aaaccc"
 * Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and
 * "aaaccc" are valid answers.
 * Note that "cacaca" is incorrect, as the same characters must be together.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "Aabb"
 * Output: "bbAa"
 * Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
 * Note that 'A' and 'a' are treated as two different characters.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 5 * 10^5
 * s consists of uppercase and lowercase English letters and digits.
 *
 *
 */

// @lc code=start
package main

import (
	"sort"
	"strings"
)

func frequencySort(s string) string {
	// return mySolution(s)
	return optimal(s)
}

func optimal(s string) string {
	freq := make(map[rune]int)
	for _, c := range s {
		freq[c]++
	}

	chars := make([]rune, 0, len(freq))
	for c := range freq {
		chars = append(chars, c)
	}

	sort.Slice(chars, func(i int, j int) bool {
		if freq[chars[i]] == freq[chars[j]] {
			return chars[i] < chars[j]
		}
		return freq[chars[i]] > freq[chars[j]]
	})

	var sb strings.Builder
	for _, c := range chars {
		for range freq[c] {
			sb.WriteRune(c)
		}
	}
	return sb.String()
}

type Mapping struct {
	char      string
	frequency int
}

func mySolution(s string) string {
	pattern := [26]*Mapping{}
	for i := range 26 {
		m := Mapping{
			char:      string(i + 'a'),
			frequency: 0,
		}
		pattern[i] = &m
	}
	for _, c := range s {
		m := pattern[c-'a']
		m.frequency++
	}
	sort.Slice(pattern[:], func(i int, j int) bool {
		return pattern[i].frequency > pattern[j].frequency
	})

	var res string
	for _, m := range pattern {
		for m.frequency > 0 {
			res += m.char
			m.frequency--
		}
	}
	return res
}

// @lc code=end
