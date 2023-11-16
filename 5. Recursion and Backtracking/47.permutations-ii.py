#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (58.00%)
# Likes:    8076
# Dislikes: 135
# Total Accepted:    829K
# Total Submissions: 1.4M
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recursionWithVisited(nums, perms=[], answer=[]):
            if not nums:
                answer.append(perms[:])

            visited = set()

            for i in range(len(nums)):
                if nums[i] not in visited: # skip if nums[i] was already considered for permutation
                    visited.add(nums[i])
                    perms.append(nums[i])
                    newNums = nums[:i] + nums[i+1:]
                    recursionWithVisited(newNums, perms)
                    perms.pop()
            return answer
        # return recursionWithVisited(nums)
        
        nums.sort()
        def recursionWithSort(nums, perms=[], answer=[]):
            if not nums:
                answer.append(perms[:])

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                perms.append(nums[i])
                recursionWithSort(nums[:i] + nums[i+1:])
                perms.pop()
            return answer
        return recursionWithSort(nums)

# @lc code=end
