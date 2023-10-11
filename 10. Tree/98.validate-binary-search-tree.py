#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (32.28%)
# Likes:    15866
# Dislikes: 1290
# Total Accepted:    2.1M
# Total Submissions: 6.4M
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
#
# A valid BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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
    prev = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Inorder Traversal of BST gives ascending order of values
        return self.iterativeIsValidBST(root)
        # return self.recursiveIsValidBST(root)

    def recursiveIsValidBST(self, root):
        if not root:
            return True

        if not self.recursiveIsValidBST(root.left):
            return False

        if self.prev and root.val <= self.prev.val:
            return False

        self.prev = root

        if not self.recursiveIsValidBST(root.right):
            return False

        return True


    def iterativeIsValidBST(self, root):
        stack = []
        prev = None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
# @lc code=end
