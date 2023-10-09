#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (74.66%)
# Likes:    12451
# Dislikes: 656
# Total Accepted:    2.2M
# Total Submissions: 2.9M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.recursiveInorderTraversal(root)
        # return self.betterRecursiveInorderTraversal(root)
        # return self.gfgIterativeInorderTraversal(root)
        return self.IterativeInorderTraversal(root)

    def recursiveInorderTraversal(self, root):
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
        return res

    def betterRecursiveInorderTraversal(self, root):
        return self.betterRecursiveInorderTraversal(root.left) + [root.val] + self.betterRecursiveInorderTraversal(root.right) if root else []

    def gfgIterativeInorderTraversal(self, root):
        stack = []
        res = []
        while True:
            if root is not None:
                stack.append(root)
                root  = root.left
            elif stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
            else:
                break
        return res

    def IterativeInorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right
# @lc code=end
