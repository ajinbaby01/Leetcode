#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (69.21%)
# Likes:    7724
# Dislikes: 206
# Total Accepted:    788.7K
# Total Submissions: 1.1M
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers
# chosen from the range [1, n].
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
# be the same combination.
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
# 1 <= k <= n
#
#
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recursion(start, comb=[], answer=[]):
            if len(comb) == k:
                answer.append(comb[:])
            for i in range(start, n+1):
                comb.append(i)
                recursion(i+1, comb)
                comb.pop()
            return answer
        return recursion(1)

#     # if the array is not [1..n] but is a given list
#     def combine(self, nums: List, k: int) -> List[List[int]]:
#         nums.sort()
#         def recursion(nums, start, comb=[], answer=[]):
#             if len(comb) == k:
#                 answer.append(comb[:])

#             visited = set() # if nums contain duplicates

#             for i in range(start, len(nums)):
#                 if nums[i] not in visited:
#                     visited.add(nums[i])
#                     comb.append(nums[i])
#                     recursion(nums, i+1, comb)
#                     comb.pop()
#             return answer
#         return recursion(nums, 0)
# print(Solution().combine([3,5,6], 2))
# @lc code=end
