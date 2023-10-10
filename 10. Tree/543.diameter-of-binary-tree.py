#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (57.90%)
# Likes:    12569
# Dislikes: 792
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the root of a binary tree, return the length of the diameter of the
# tree.
#
# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges
# between them.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#
#
# Example 2:
#
#
# Input: root = [1,2]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # return self.recursiveDiameterOfBinaryTree(root)
        return self.betterRecursiveDiameterOfBinaryTree(root)

    def betterRecursiveDiameterOfBinaryTree(self, root):
        # Starts from the leaf node and goes back to root
        # Find the diameter of subtree through that node
        # Return max depth from left and right subtree to parent node
        # The path of traversal is similar to the problem Balanced Binary Tree
        self.diameter = 0

        def depth(root):
            if not root:
                return 0
            left, right = depth(root.left), depth(root.right)
            current_diameter = left + right
            self.diameter = max(current_diameter, self.diameter)

            # returns max depth of subtree to parent node
            return 1 + max(left, right)

        depth(root)
        return self.diameter
    # Time: O(n)

    def recursiveDiameterOfBinaryTree(self, root):
        # Starts from root and goes to leaf
        # Go through all the nodes
        # For each node as root, calculate the diameter through the node
        # diameter = sum of max depth of left and right subtree
        # Check if current diameter is bigger than max diameter
        self.diameter = 0

        def dfs(root): # Function to go though all nodes in a dfs manner
            if root:
                current_diameter = self.depth(root.left) + self.depth(root.right)
                self.diameter = max(current_diameter, self.diameter)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return self.diameter
    # Time: O(n^2)

    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
# @lc code=end
