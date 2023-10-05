#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
#
# algorithms
# Medium (39.85%)
# Likes:    2917
# Dislikes: 80
# Total Accepted:    54.1K
# Total Submissions: 135.7K
# Testcase Example:  '[1,2,4]\n5'
#
# The frequency of an element is the number of times it occurs in an array.
#
# You are given an integer array nums and an integer k. In one operation, you
# can choose an index of nums and increment the element at that index by 1.
#
# Return the maximum possible frequency of an element after performing at most
# k operations.
#
#
# Example 1:
#
#
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element
# two times to make nums = [4,4,4].
# 4 has a frequency of 3.
#
# Example 2:
#
#
# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a
# frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a
# frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a
# frequency of 2.
#
#
# Example 3:
#
#
# Input: nums = [3,9,6], k = 2
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= k <= 10^5
#
#
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums, k):
        left = 0
        nums.sort()
        for right in range(len(nums)):
            k += nums[right]
            if k < nums[right] * (right - left + 1):
                k -= nums[left]
                left += 1
        return right - left + 1
# the size of window keeps increasing as long as it is valid.
# during any expansion, if window is invalid, window size is reduced (left+=1)
# For eg: at one point the window is [1,3,5,7] (size = 4).
# But the window size is reduced as that window is invalid
# At the end the window right and left points to is [101, 102, 103]
# But this is not the correct window
# Correct window is [100, 101, 102]
# But the size of the window remains the same (3)
print(Solution().maxFrequency([1, 3, 5, 7, 100, 101, 102, 103], 6))

# After the valid window [4,5,6,7] is found, whenever right points to the fifth element
# left is increased to keep the window size 4
print(Solution().maxFrequency([4, 5, 6, 7, 100, 101, 102, 103], 6))

# In this code, after a valid window is found [4,5,6,7] (size = 4), the size (right-left+1) is increased only
# if another valid window whose size is greater than current window is found [9, 9, 10, 10, 11] (size = 5).
# The size is never decreased after a valid window is found, only increased.
print(Solution().maxFrequency([4, 5, 6, 7, 9, 9, 10, 10, 11, 100, 101, 102, 103], 6))


# @lc code=end
