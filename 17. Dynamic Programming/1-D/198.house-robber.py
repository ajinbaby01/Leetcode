#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (50.21%)
# Likes:    20739
# Dislikes: 411
# Total Accepted:    2.2M
# Total Submissions: 4.3M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = no_rob = 0
        # Go through each house
        for num in nums:
            # If you rob current house,
            # add value to no_rob since no_rob represents not stealing from adjacent/previous house
            new_rob = no_rob + num

            # If you don't rob current house,
            new_no_rob = max(rob, no_rob)

            # Update the values of rob and no_rob
            rob, no_rob = new_rob, new_no_rob

        # Choose whether to rob the last house or not
        return max(rob, no_rob)
# @lc code=end
