/*
 * @lc app=leetcode id=128 lang=golang
 *
 * [128] Longest Consecutive Sequence
 *
 * https://leetcode.com/problems/longest-consecutive-sequence/description/
 *
 * algorithms
 * Medium (47.28%)
 * Likes:    22011
 * Dislikes: 1190
 * Total Accepted:    2.8M
 * Total Submissions: 6M
 * Testcase Example:  '[100,4,200,1,3,2]'
 *
 * Given an unsorted array of integers nums, return the length of the longest
 * consecutive elements sequence.
 *
 * You must write an algorithm that runs in O(n) time.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [100,4,200,1,3,2]
 * Output: 4
 * Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
 * Therefore its length is 4.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [0,3,7,2,5,8,4,6,0,1]
 * Output: 9
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [1,0,1,2]
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 *
 *
 */

// @lc code=start
func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	hashMap := make(map[int]struct{})
	longest := 1
	for _, num := range nums {
		hashMap[num] = struct{}{}
	}

	for num, _ := range hashMap {
		if _, ok := hashMap[num-1]; !ok {
			i := num + 1
			for _, ok := hashMap[i]; ok; _, ok = hashMap[i] {
				i++
			}
			longest = max(longest, i-num) // longestStart can be found here
		}
	}

	return longest

	// longestSeq := make([]int, longest)
 	// for i := 0; i < longest; i++ {
 	// 	longestSeq[i] = longestStart + i
 	// }
 	// return longestSeq
}

// @lc code=end
