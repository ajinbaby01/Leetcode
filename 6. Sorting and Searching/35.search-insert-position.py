#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (45.00%)
# Likes:    15843
# Dislikes: 715
# Total Accepted:    2.9M
# Total Submissions: 6.2M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
#
# Example 2:
#
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
#
# Example 3:
#
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
#
#
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    # Time: O(logn), Space: O(1)
# @lc code=end
