#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (59.01%)
# Likes:    21510
# Dislikes: 3599
# Total Accepted:    1.4M
# Total Submissions: 2.3M
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only
# constant extra space.
#
#
# Example 1:
#
#
# Input: nums = [1,3,4,2,2]
# Output: 2
#
#
# Example 2:
#
#
# Input: nums = [3,1,3,4,2]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
#
#
#
# Follow up:
#
#
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
#
#
#

# @lc code=start
class Solution:
    # Since only one number is repeated, a negative number is visited
    # a second time only if the idx is repeated
    # def findDuplicate(self, nums: List[int]) -> int:
    #     for num in nums:
    #         idx = abs(num)
    #         val = nums[idx]
    #         if val < 0:
    #             return idx
    #         nums[idx] = -val
    # Time: O(n), Space: O(1), Modified array

########################################################################

    # If the array is sorted, nums[i] == i + 1
    # If element is not at correct index, we move it to correct index
    # If the element is not at correct index and the element at the correct index
    # is equal to current element, it's the repeated element
    # def findDuplicate(self, nums: List[int]) -> int:
    #     i = 0
    #     while True:
    #         n = nums[i]
    #         if n == i + 1:
    #             i += 1
    #         elif n == nums[n - 1]:
    #             return n
    #         else:
    #             nums[i], nums[n - 1] = nums[n - 1], nums[i]
    # Time: O(n), Space: O(1), Modified array

########################################################################

    # Binary search on the range [1..n]
    #
    # def findDuplicate(self, nums: List[int]) -> int:
    #     left = 1
    #     right = len(nums) - 1
    #     while left <= right:  O(logn)
    #         mid = (left + right) // 2
    #         count = 0
    #         for num in nums: O(n)
    #             if num <= mid:
    #                 count += 1
    #         if count > mid:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return left
    # Time: O(nlogn), Space: O(1), Array not modified

########################################################################

    # Linked list and Floyd's Algorithm
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
    # Time: O(n), Space: O(1)
# @lc code=end
