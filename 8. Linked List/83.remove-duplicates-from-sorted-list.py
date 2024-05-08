#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (51.87%)
# Likes:    8568
# Dislikes: 297
# Total Accepted:    1.5M
# Total Submissions: 2.9M
# Testcase Example:  '[1,1,2]'
#
# Given the head of a sorted linked list, delete all duplicates such that each
# element appears only once. Return the linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,1,2]
# Output: [1,2]
#
#
# Example 2:
#
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.storeDuplicates(head)
        return self.optimalSolution(head)

    def optimalSolution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head # Copy head
        while cur:
            # cur and cur.next has the same value (duplicates)
            while cur.next and cur.val == cur.next.val:
                # Skip the duplicate node
                cur.next = cur.next.next
            # Either cur.next is None or we found a unique node
            cur = cur.next
        return head

    def storeDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicates = set()
        ans = head
        while head is not None:
            if head.val not in duplicates:
                duplicates.add(head.val)
                prev = head
            else:
                prev.next = head.next
            head = head.next
        return ans
# @lc code=end
