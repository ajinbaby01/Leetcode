#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (63.03%)
# Likes:    11314
# Dislikes: 411
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Return head if no nodes or only one node
        if not head or head.next:
            return head

        curr = nxt = head
        head = head.next
        # In each loop two adjacent nodes are swapped
        # In the subsequent loop, we need to update the next part
        # of the previous loop. Prev keeps track of the node to be updated
        # In the first loop, the head node doesn't have a previous node
        # So, we make prev as a dummy node that points to head
        prev = ListNode(0, head)

        # curr becomes None for even numbers of nodes
        # curr.next becomes None for odd number of nodes
        while curr and curr.next:
            # curr and nxt are two adjacent nodes to be swapped
            nxt = curr.next

            # Swapping the nodes by updating the links
            curr.next = nxt.next
            nxt.next = curr

            # Updating prev from previous loop to point to the swapped node in current loop
            prev.next = nxt

            # Changing prev to use in the next loop
            prev = curr

            # Moving the next pair of nodes to be swapped
            curr = curr.next

        # Returning the head (updated to head.next) which is always the second node (for n >= 2)
        return head
# @lc code=end
