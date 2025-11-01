/*
Problem Statement: You are given a string s and a positive integer k.
Return the number of substrings that contain exactly k distinct characters.

Example 1:
Input: s = "pqpqs", k = 2
Output: 7
Explanation:  All substrings with exactly 2 distinct characters:
"pq", "pqp", "pqpq", "qp", "qpq", "pqs", "qs"
Total = 7.

Example 2:
Input: s = "abcbaa", k = 3
Output: 5
Explanation:  All substrings with exactly 3 distinct characters:
"abc", "abcb", "abcba", "bcba", "cbaa"
Total = 5.

Algorithm
1. Define a helper function atMostKDistinct(s, k):
2. Use a sliding window with two pointers (left and right) and a frequency map.
3. Expand the window by moving the right pointer and count characters.
4. If the count of distinct characters exceeds k, shrink the window by moving the left pointer.
5. For each valid window, add (right - left + 1) to the result.
6. To find substrings with exactly k distinct characters, calculate:
7. atMostKDistinct(s, k) - atMostKDistinct(s, k-1)
*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(countSubstring("pqpqs", 2))
}

func countSubstring(s string, k int) int {
	return atMostKDistinct(s, k) - atMostKDistinct(s, k-1)
}

func atMostKDistinct(s string, k int) int {
	left, res := 0, 0
	freq := make(map[byte]int)

	for right := range s {
		freq[s[right]]++
		for len(freq) > k {
			freq[s[left]]--
			if freq[s[left]] == 0 {
				delete(freq, s[left])
			}
			left++
		}
		res += (right - left + 1)
	}
	return res
}
