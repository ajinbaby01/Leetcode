#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (46.46%)
# Likes:    6926
# Dislikes: 1243
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
#
# Example 2:
#
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^5].
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        # Here we go through all the paths
        # Then we find all the leaf nodes and calculate the depths of all leaves
        # Then we compare the depths and find the min depth
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # if not root.left:
        #     return 1 + self.minDepth(root.right)
        # if not root.right:
        #     return 1+ self.minDepth(root.left)
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        # It isn't necessary to find the depths of all leaf nodes
        # We can traverse in level-order and the instant we find a leaf node,
        # we can return the current depth as min depth
        # Thus, we eliminate finding the depths of all leaf nodes
        # We are essentially looking for the first leaf node in level-order traversal
        # https://www.youtube.com/watch?v=tZS4VHtbYoo

        # BFS (Level-Order Traversal)
        if not root:
            return 0
        q = collections.deque()
        depth = 1
        q.append((root, depth))
        while True:
            node, depth = q.popleft()
            if not node.right and not node.left:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
# @lc code=end
