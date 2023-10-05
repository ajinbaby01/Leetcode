#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (59.85%)
# Likes:    29115
# Dislikes: 415
# Total Accepted:    1.7M
# Total Submissions: 2.8M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # # water at index i = min(left_max_of_i, right_max_of_i) - height[i]
        # n = len(height)
        # total_water = 0

        # left_max = [0]*n
        # right_max = [0]*n
        # # left_max[i] stores the maximum height to the left of i
        # # right_max[i] stores the maximum height to the right of i

        # tallest_left = 0
        # tallest_right = 0
        # for i in range(n):
        #     left_max[i] = max(tallest_left, height[i])
        #     tallest_left = left_max[i]

        #     right_max[n-i-1] = max(tallest_right, height[n-i-1])
        #     tallest_right = right_max[n-i-1]

        # for i in range(n):
        #     water_at_index_i = min(left_max[i], right_max[i]) - height[i]
        #     total_water += water_at_index_i

        # return total_water
        # # Time: O(n), Space: O(n)

        # Using two pointers. Watch Take U Forward explanation
        n = len(height)
        total_water = 0
        left, right = 0, n - 1
        left_max, right_max = 0, 0

        while left <= right:
            if height[left] <= height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1
        return total_water
        # Time: O(n), Space: O(1)
# @lc code=end
