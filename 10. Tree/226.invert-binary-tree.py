#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (75.64%)
# Likes:    13173
# Dislikes: 186
# Total Accepted:    1.8M
# Total Submissions: 2.3M
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Given the root of a binary tree, invert the tree, and return its root.
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
#
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
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

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # return self.recursiveDFS(root)
        # return self.iterativeDFS(root)
        return self.BFS(root)

    def recursiveDFS(self, root):
        if not root:
            return
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.right)
        # self.invertTree(root.left)
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def iterativeDFS(self, root):
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            node.right, node.left = node.left, node.right
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root

    def BFS(self, root):
        if not root:
            return

        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.right, node.left = node.left, node.right
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return root
# @lc code=end
