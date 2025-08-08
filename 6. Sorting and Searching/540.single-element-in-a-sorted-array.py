#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (59.02%)
# Likes:    10215
# Dislikes: 157
# Total Accepted:    531.8K
# Total Submissions: 901K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.
#
#
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    # In a sorted array where all elements appear twice except for one:
    # Before the unique element, the first occurrence of a pair is at an even index, and the second is at an odd index.
    # After the unique element, this pattern is disrupted.
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # Make sure mid is even so its pair is mid ^ 1 (flip last bit)
            if mid % 2 == 1:
                mid -= 1

            # If pair is correct, move to right half
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


# @lc code=end
