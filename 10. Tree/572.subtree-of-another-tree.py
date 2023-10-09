#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (46.93%)
# Likes:    7763
# Dislikes: 452
# Total Accepted:    730.9K
# Total Submissions: 1.6M
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and
# false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.
#
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # return self.iterativeIsSubTree(root, subRoot)
        return self.recursiveIsSubTree(root, subRoot)

    def recursiveIsSubTree(self, root, subRoot):
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True
        return (self.recursiveIsSubTree(root.left, subRoot) or
                self.recursiveIsSubTree(root.right, subRoot))

    def iterativeIsSubTree(self, root, subRoot):
        # For every node in the bigger tree, check if that is the subtree
        # with subRoot as the root node
        # Inorder traverse the bigger tree
        # For each node, check if that becomes the subtree
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return False
            root = stack.pop()
            if(self.isSameTree(root, subRoot)):
                return True
            root = root.right

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))
# @lc code=end
