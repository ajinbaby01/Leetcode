#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
#
# algorithms
# Medium (73.59%)
# Likes:    5394
# Dislikes: 139
# Total Accepted:    386.7K
# Total Submissions: 526.5K
# Testcase Example:  '[3,1,4,3,null,1,5]'
#
# Given a binary tree root, a node X in the tree is named good if in the path
# from root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.
#
#
# Example 1:
#
#
#
#
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
#
# Example 2:
#
#
#
#
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
#
# Example 3:
#
#
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
#
#
# Constraints:
#
#
# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].
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
    def goodNodes(self, root: TreeNode) -> int:
        # return self.neetcodeGoodNodes(root)
        return self.myGoodNodes(root)

    def myGoodNodes(self, root):
        # Traverse each path
        # Keep track of the maximum in the path
        # If value of current node is equal or greater than the maximum
        # update maximum and increment count
        self.count = 0
        def dfs(root, curMax):
            if not root:
                return
            if root.val >= curMax:
                self.count += 1
                curMax = root.val
            dfs(root.left, curMax)
            dfs(root.right, curMax)
        dfs(root, root.val)
        return self.count

    def neetcodeGoodNodes(self, root):
        def dfs(root, curMax):
            if not root:
                return 0
            if root.val >= curMax:
                count = 1
                curMax = root.val
            else:
                count = 0

            # Add number of good nodes from left and right subtree to root count
            count += dfs(root.left, curMax)
            count += dfs(root.right, curMax)
            return count

        return dfs(root, root.val)
# @lc code=end
