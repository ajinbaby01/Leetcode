#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (42.43%)
# Likes:    17192
# Dislikes: 706
# Total Accepted:    2.2M
# Total Submissions: 5.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#
# Follow up: Could you do this in one pass?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # Getting length of list
        # i = 0
        # head1= head
        # while head1:
        #     i += 1
        #     head1 = head1.next

        # # Checking if node to be removed is the first node
        # if i == n:
        #     head = head.next
        #     return head

        # # Decrementing i and checking if ith node from end is to be removed
        # head1 = head
        # while head1:
        #     prev = head1
        #     head1 = head1.next
        #     i -= 1
        #     if i == n:
        #         prev.next = head1.next
        #         return head

        slow = fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
# @lc code=end
