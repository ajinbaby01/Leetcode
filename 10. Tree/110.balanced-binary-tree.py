#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (50.30%)
# Likes:    9935
# Dislikes: 576
# Total Accepted:    1.3M
# Total Submissions: 2.5M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
# Example 3:
#
#
# Input: root = []
# Output: true
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # return self.recursiveIsBalanced(root)
        return self.betterRecursiveIsBalanced(root)

    def betterRecursiveIsBalanced(self, root):
        # Starts from the bottom
        # Check if bottom subtrees are balanced.
        # If balanced, return height from both subtrees
        # Else return -1
        # Watch neetcode video: https://www.youtube.com/watch?v=QfJsau0ItOY
        # Then implement https://leetcode.com/problems/balanced-binary-tree/solutions/35708/very-simple-python-solutions-iterative-and-recursive-both-beat-90/
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)

            # left subtree of root is unbalanced or
            # right subtree of root is unbalanced or
            # root tree is unbalanced
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            # if balanced, return the depth of root tree
            return 1 + max(left, right)

        # -1 means tree is unbalanced
        return dfs(root) != -1
    # Time: O(n)

    def recursiveIsBalanced(self, root):
        # For every node, check if it's left and right subtree is balanced
        if not root:
            return True
        diff = abs(self.depth(root.left) - self.depth(root.right))
        if diff > 1: # root tree is unbalanced
            return False

        # if root is balanced, check if both subtrees are balanced
        # because a root can be balanced but the subtree may not be
        return (self.recursiveIsBalanced(root.left) and self.recursiveIsBalanced(root.right))
    # Time: O(n^2)

    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
# @lc code=end
