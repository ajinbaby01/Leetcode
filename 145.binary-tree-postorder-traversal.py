#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (69.32%)
# Likes:    6483
# Dislikes: 182
# Total Accepted:    1.1M
# Total Submissions: 1.5M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
# The number of the nodes in the tree is in the range [0, 100].
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.recursivePostorderTraversal(root)
        # return self.betterRecursivePostorderTraversal(root)
        # return self.iterativePostorderTraversal(root)
        return self.betterIterativePostorderTraversal(root)

    def recursivePostorderTraversal(self, root):
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                res.append(root.val)
        dfs(root)
        return res

    def betterRecursivePostorderTraversal(self, root):
        return self.betterRecursivePostorderTraversal(root.left) + self.betterRecursivePostorderTraversal(root.right) + [root.val] if root else []

    def iterativePostorderTraversal(self, root):
        if not root:
            return []
        stack1, stack2, res = [root], [], []
        while stack1:
            root = stack1.pop()
            stack2.append(root)

            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)

        while stack2:
            root = stack2.pop()
            res.append(root.val)

        return res

    def betterIterativePostorderTraversal(self, root):
        if not root:
            return []

        stack, res = [(root, False)], []

        while stack:
            root, visited = stack.pop()
            if visited:
                res.append(root.val)
            else:
                stack.append((root, True))
                if root.right:
                    stack.append((root.right, False))
                if root.left:
                    stack.append((root.left, False))
        return res
# @lc code=end
