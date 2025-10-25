/*
 * @lc app=leetcode id=69 lang=golang
 *
 * [69] Sqrt(x)
 *
 * https://leetcode.com/problems/sqrtx/description/
 *
 * algorithms
 * Easy (38.26%)
 * Likes:    8008
 * Dislikes: 4468
 * Total Accepted:    1.9M
 * Total Submissions: 5M
 * Testcase Example:  '4'
 *
 * Given a non-negative integer x, return the square root of x rounded down to
 * the nearest integer. The returned integer should be non-negative as well.
 *
 * You must not use any built-in exponent function or operator.
 *
 *
 * For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: x = 4
 * Output: 2
 * Explanation: The square root of 4 is 2, so we return 2.
 *
 *
 * Example 2:
 *
 *
 * Input: x = 8
 * Output: 2
 * Explanation: The square root of 8 is 2.82842..., and since we round it down
 * to the nearest integer, 2 is returned.
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= x <= 2^31 - 1
 *
 *
 */

// @lc code=start
package main

import "math"

func mySqrt(x int) int {
	return binarySearch(x)
	// return babylonian(x)
}

// For nearest integer
func binarySearch(x int) int {
	left, right := 1, x
	for left <= right {
		mid := left + (right-left)/2
		if mid*mid < x {
			left = mid + 1
		} else if mid * mid > x {
			right = mid - 1
		} else {
			return mid
		}
	}
	return right
}

func babylonian(x int) int {
	if x == 0 {
		return 0
	}
	precision := 0.01
	num := float64(x)
	guess := num / 2
	for {
		newGuess := (guess + num / guess) / 2
		if math.Abs(guess - newGuess) < precision {
			return int(math.Floor(newGuess))
		}
		guess = newGuess
	}
}

// @lc code=end
