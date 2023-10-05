#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (37.11%)
# Likes:    15041
# Dislikes: 1678
# Total Accepted:    939K
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array nums, return the smallest missing positive
# integer.
#
# You must implement an algorithm that runs in O(n) time and uses O(1)
# auxiliary space.
#
#
# Example 1:
#
#
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#
#
# Example 2:
#
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#
#
# Example 3:
#
#
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        # missing = 1
        # for num in nums:
        #     if missing == num:
        #         missing += 1
        # return missing
        # Time: O(nlogn), Space: O(1)

        n = len(nums)
        dic = set()

        for i in range(n):
            dic.add(nums[i])

        for num in range(1, n+2):
            if num not in dic:
                return num
        # Time: O(n), Space: O(n)

        # The solution of O(n) time and O(1) space is hard.
        # One technique is to use the given 'nums' to hash the numbers
        # nums[nums[i] % n] += n
        
# @lc code=end
