#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (54.29%)
# Likes:    9656
# Dislikes: 318
# Total Accepted:    744.1K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
# Reorder the list to be on the following form:
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1->2->None and 4->3->None
        # 1->2->None and 5->4->None
        # slow = fast = head
        # while fast and fast.next:
        #     prev = slow
        #     slow = slow.next
        #     fast = fast.next.next
        # if slow == fast:
        #     return head
        # prev.next = None
        # prev = None
        # while slow:
        #     nxt = slow.next
        #     slow.next = prev
        #     prev = slow
        #     slow = nxt
        # head2 = prev
        # head1 = head
        # while head1:
        #     nxt1 = head1.next
        #     nxt2 = head2.next
        #     head1.next = head2
        #     if nxt1:
        #         head2.next = nxt1
        #     head1 = nxt1
        #     head2 = nxt2
        # return head

        # In the below method, we make the bigger list be the first list
        # Eg: 1->2->3->None and 4->None
        # Eg: 1->2->3->None and 5->4->None
        # Makes it easier
        # Splitting the lists into two
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            return head
        head2 = slow.next
        slow.next = None

        # Reversing the second list
        prev = None
        while head2:
            nxt = head2.next
            head2.next = prev
            prev = head2
            head2 = nxt
        head2 = prev
        head1 = head

        # Merging the two lists
        while head2:
            nxt1 = head1.next
            nxt2 = head2.next
            head1.next = head2
            head2.next = nxt1
            head1 = nxt1
            head2 = nxt2
        return head
# @lc code=end
