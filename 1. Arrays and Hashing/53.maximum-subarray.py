#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (50.86%)
# Likes:    36209
# Dislikes: 1535
# Total Accepted:    5.2M
# Total Submissions: 10M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # return self.doubleLoop(nums)
        # return self.maxSumWithIndex(nums)
        return self.kadaneAlgo(nums)

    def maxSumWithIndex(self, nums):
        maxSum = nums[0]
        currSum = 0
        maxLeft, maxRight, left = 0, 0, 0
        for right in range(len(nums)):
            if currSum < 0:
                currSum = 0
                left = right
            currSum += nums[right]
            if maxSum < currSum:
                maxLeft, maxRight = left, right
                maxSum = currSum
        return maxSum, maxLeft, maxRight

    def kadaneAlgo(self, nums):
        maxSum = nums[0]
        # currSum tracks the sum of sub array before the position of num
        # If currSum is negative, that means the sub array sum is negative and can be ignored
        # Hence, currSum is reset to 0 and currSum now tracks the sub array starting from num
        currSum = 0
        for num in nums:
            currSum = max(currSum, 0)
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum

    def doubleLoop(self, nums):
        maxSum = nums[0]
        for i in range(len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                summ += nums[j]
                maxSum = max(summ, maxSum)
        return maxSum
# @lc code=end
