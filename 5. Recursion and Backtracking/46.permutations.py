#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (77.15%)
# Likes:    17848
# Dislikes: 289
# Total Accepted:    1.8M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
#
#
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Using backtracking. One one perm variable is maintained
        def recursion(nums, perms=[], answer=[]):
            if len(nums) == 0:
                answer.append(perms[:])

            for i in range(len(nums)):
                perms.append(nums[i])
                newNums = nums[:i] + nums[i+1:]
                recursion(newNums)
                perms.pop()
            return answer

        # # Avoided backtracking by maintaining multiple perm snapshots
        # def recursion(nums, perms=[], answer=[]):
        #     if len(nums) == 0:
        #         answer.append(perms)

        #     for i in range(len(nums)):
        #         # perms.append(nums[i])
        #         newNums = nums[:i] + nums[i+1:]
        #         recursion(newNums, perms + [nums[i]])
        #         # perms.pop()
        #     return answer
        return recursion(nums)

# @lc code=end
