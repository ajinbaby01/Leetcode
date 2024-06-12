#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (78.96%)
# Likes:    8746
# Dislikes: 301
# Total Accepted:    772.5K
# Total Submissions: 978.2K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the
# two trees are overlapped while the others are not. You need to merge the two
# trees into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise, the
# NOT null node will be used as the node of the new tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.
#
#
# Example 1:
#
#
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#
#
# Example 2:
#
#
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
#
#
#
# Constraints:
#
#
# The number of nodes in both trees is in the range [0, 2000].
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # return self.recursive(root1, root2)
        return self.iterative(root1, root2)
    
    def recursive(self, root1, root2):
        # If both root1 and root2 exists, take their sum and update root1.
        # Update left and right child of root1 with either the sum or one of the existing nodes if other is None,
        # since if either root1 or root2 is None, not None root is returned.
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        else:
            return root1 or root2
    
    def iterative(self, root1, root2):
        # If one tree is empty, return the other
        if not root2 or not root1:
            return root1 or root2
        
        stack = [(root1, root2)]
        while stack:
            t1, t2 = stack.pop()

            # We update the nodes of t1.
            # If t2 is empty, nodes are not overlapping and we can skip.
            if not t2:
                continue
            
            # Add the values of overlapping nodes together
            t1.val += t2.val

            # We only add childern of t1(t1.left/t1.right) to stack if it exists.
            # If child is None, we place the child of t2(t2.left/t2.right) in that position.
            # Child of t2(t2.left/t2.right) can be None. In that case, tree remains unchanged.
            # Eg: t1.left = t2.left => t1.left = None. t1.left was already None(tree unchanged)
            if t1.left:
                stack.append((t1.left, t2.left))
            else:
                t1.left = t2.left
            
            if t1.right:
                stack.append((t1.right, t2.right))
            else:
                t1.right = t2.right
                
        return root1
# @lc code=end
