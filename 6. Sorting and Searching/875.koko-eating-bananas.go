/*
 * @lc app=leetcode id=875 lang=golang
 *
 * [875] Koko Eating Bananas
 *
 * https://leetcode.com/problems/koko-eating-bananas/description/
 *
 * algorithms
 * Medium (48.69%)
 * Likes:    12873
 * Dislikes: 854
 * Total Accepted:    1.3M
 * Total Submissions: 2.7M
 * Testcase Example:  '[3,6,7,11]\n8'
 *
 * Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
 * piles[i] bananas. The guards have gone and will come back in h hours.
 *
 * Koko can decide her bananas-per-hour eating speed of k. Each hour, she
 * chooses some pile of bananas and eats k bananas from that pile. If the pile
 * has less than k bananas, she eats all of them instead and will not eat any
 * more bananas during this hour.
 *
 * Koko likes to eat slowly but still wants to finish eating all the bananas
 * before the guards return.
 *
 * Return the minimum integer k such that she can eat all the bananas within h
 * hours.
 *
 *
 * Example 1:
 *
 *
 * Input: piles = [3,6,7,11], h = 8
 * Output: 4
 *
 *
 * Example 2:
 *
 *
 * Input: piles = [30,11,23,4,20], h = 5
 * Output: 30
 *
 *
 * Example 3:
 *
 *
 * Input: piles = [30,11,23,4,20], h = 6
 * Output: 23
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= piles.length <= 10^4
 * piles.length <= h <= 10^9
 * 1 <= piles[i] <= 10^9
 *
 *
 */

// @lc code=start
package main

import "math"

func minEatingSpeed(piles []int, h int) int {
	left, right := 1, findMaxPile(piles)
	minEatingSpeed := right
	for left <= right {
		mid := (left + right) / 2

		if isKValid(piles, mid, h) {
			minEatingSpeed = mid
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return minEatingSpeed
}

func isKValid(piles []int, k, h int) bool {
	totalTime := 0
	for _, pile := range piles{
		totalTime += int(math.Ceil(float64(pile) / float64(k)))
	}
	return totalTime <= h
}

func findMaxPile(piles []int) int {
	var maxPile int
	for _, pile := range piles {
		maxPile = max(maxPile, pile)
	}
	return maxPile
}
// @lc code=end
