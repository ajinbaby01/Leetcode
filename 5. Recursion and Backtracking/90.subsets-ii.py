#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (56.47%)
# Likes:    9012
# Dislikes: 249
# Total Accepted:    777.7K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
#
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def recursionWithVisited(nums, path=[], answer=[]):
            answer.append(path)

            visited = set()

            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    recursionWithVisited(nums[i+1:], path + [nums[i]])
            return answer
        # return recursionWithVisited(nums)

        def recursionWithWhileLoop(nums, path=[], answer=[]):
            answer.append(path[:])

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                recursionWithWhileLoop(nums[i+1:])
                path.pop()
            return answer
        return recursionWithWhileLoop(nums)

# @lc code=end
