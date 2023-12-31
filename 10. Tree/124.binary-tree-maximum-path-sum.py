#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (39.48%)
# Likes:    15626
# Dislikes: 678
# Total Accepted:    1.1M
# Total Submissions: 2.7M
# Testcase Example:  '[1,2,3]'
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty
# path.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
# = 42.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Same principle as finding max diameter (start from leaf node and work towards root)
        # Instead of returning 1 + max depth between left and right subtree,
        # we return root.val + max value between left and right subtree
        self.maxPath = root.val # set maxPath = 0 to see which test case fails
        def dfs(root):
            if not root:
                return 0
            # left and right values can never be negative because of how we return value
            left, right = dfs(root.left), dfs(root.right)
            self.maxPath = max(self.maxPath, root.val + left + right)
            # Ensures min value for left and right is 0
            return max(0, root.val + max(left, right))
        dfs(root)
        return self.maxPath

    def maxPathSumWithPath(self, root):
        # Gives the path (not in order)
        self.maxSum = root.val
        self.maxPath = [root.val]

        def dfs(root):
            if not root:
                return 0, []

            left_sum, left_path = dfs(root.left)
            right_sum, right_path = dfs(root.right)

            current_sum = root.val + left_sum + right_sum
            current_path = [root.val]

            if left_sum > 0:
                current_path.extend(left_path)
            if right_sum > 0:
                current_path.extend(right_path)

            if current_sum > self.maxSum:
                self.maxSum = current_sum
                self.maxPath = current_path
                # This current_path is root.left + root + root.right

            current_path = [root.val]
            if left_sum > right_sum:
                current_path.extend(left_path)
            else:
                current_path.extend(right_path)
            # We return root + max(root.left, root.right) as new current_path

            return max(0, root.val + max(left_sum, right_sum)), current_path

        dfs(root)
        print(self.maxPath)
        return self.maxSum
# @lc code=end
