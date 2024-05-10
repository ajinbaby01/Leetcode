#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (47.89%)
# Likes:    8217
# Dislikes: 236
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
#
#
# Example 1:
#
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
#
# Example 2:
#
#
# Input: head = [], val = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= val <= 50
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return dummy.next

        # Initial solution
        # For cases when node to be deleted is the first node
        # Here, prev will point to the actual node in the first iteration
        # dummy = ListNode()
        # dummy.next = head
        # prev = dummy
        # cur = head
        # while cur:
        #     while cur.next and cur.next.val == val:
        #         cur.next = cur.next.next
        #     if cur.val == val:
        #         prev.next = cur.next
        #     prev = cur
        #     cur = cur.next
        # return dummy.next


# @lc code=end
