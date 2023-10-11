#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (62.45%)
# Likes:    14036
# Dislikes: 427
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
#
#
# Example 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
#
# Example 2:
#
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
#
# Constraints:
#
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.neetcodeBuildTree(preorder, inorder)
        # return self.simpleBuildTree(preorder, inorder)

    def neetcodeBuildTree(self, preorder, inorder):
        if preorder: # len(preorder) = len(inorder)
            idx = inorder.index(preorder[0])
            root = TreeNode(preorder[0])
            root.left = self.neetcodeBuildTree(preorder[1:idx+1], inorder[:idx])
            root.right = self.neetcodeBuildTree(preorder[idx+1:], inorder[idx + 1:])
            return root

    def simpleBuildTree(self, preorder, inorder):
        # https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
        if inorder: # len(preorder) != len(inorder)
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            root.left = self.simpleBuildTree(preorder, inorder[:idx])
            root.right = self.simpleBuildTree(preorder, inorder[idx+1:])
            return root
# @lc code=end
