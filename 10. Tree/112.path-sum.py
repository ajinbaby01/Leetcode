#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (49.62%)
# Likes:    9575
# Dislikes: 1090
# Total Accepted:    1.4M
# Total Submissions: 2.9M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the
# path equals targetSum.
#
# A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
#
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
#
#
# Example 3:
#
#
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path_sum = 0

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # return self.recursiveDFS(root, targetSum)
        return self.betterRecursion(root, targetSum)

    def betterRecursion(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        targetSum -= root.val

        return self.betterRecursion(root.left, targetSum) or self.betterRecursion(root.right, targetSum)

    def recursiveDFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Each recursive call has its own path_sum value
        # Hence, no need to subtract root.val at the end of each call
        def dfs(root, path_sum):
            if not root:
                return False

            path_sum += root.val
            if not root.left and not root.right:
                return path_sum == targetSum

            return dfs(root.left, path_sum) or dfs(root.right, path_sum)

        return dfs(root, 0)

        # Initial thought process
        # def dfs(root):
        #     if not root:
        #         return False

        #     self.path_sum += root.val
        #     if not root.left and not root.right and self.path_sum == targetSum:
        #         return True
        #     if dfs(root.left):
        #         return True
        #     if dfs(root.right):
        #         return True
        #     self.path_sum -= root.val
        # return dfs(root)
# @lc code=end
