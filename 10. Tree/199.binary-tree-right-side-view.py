#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (62.20%)
# Likes:    11117
# Dislikes: 736
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
#
# Example 2:
#
#
# Input: root = [1,null,3]
# Output: [1,3]
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # return self.myRightSideView(root)
        return self.betterRightSideView(root)

    def betterRightSideView(self, root):
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)
        return res


    def myRightSideView(self, root):
        if not root:
            return []
        res = []
        q = collections.deque()
        current_depth = 1
        q.append((root, current_depth))
        while q:
            while q and q[0][1] == current_depth:
                node, depth = q.popleft()
                if node.left:
                    q.append((node.left, depth + 1))
                if node.right:
                    q.append((node.right, depth + 1))
            res.append(node.val)
            current_depth += 1

        return res
# @lc code=end
