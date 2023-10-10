#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (65.57%)
# Likes:    14388
# Dislikes: 288
# Total Accepted:    2M
# Total Submissions: 3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
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
# The number of nodes in the tree is in the range [0, 2000].
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # return self.myOwnLevelOrder(root)
        return self.betterLevelOrder(root)

    def betterLevelOrder(self, root):
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        res = []

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res

    def myOwnLevelOrder(self, root):
        if not root:
            return []

        q = collections.deque()
        current_depth = 1
        level = []
        res = []
        q.append((root, current_depth))

        while q:
            node, depth = q.popleft()
            if depth != current_depth:
                current_depth = depth
                res.append(level)
                level = []
            level.append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        res.append(level)
        return res
# @lc code=end
