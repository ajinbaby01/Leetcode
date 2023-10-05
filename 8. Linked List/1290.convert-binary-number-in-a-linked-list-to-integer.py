#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
#
# algorithms
# Easy (81.55%)
# Likes:    3953
# Dislikes: 148
# Total Accepted:    415.2K
# Total Submissions: 509.4K
# Testcase Example:  '[1,0,1]'
#
# Given head which is a reference node to a singly-linked list. The value of
# each node in the linked list is either 0 or 1. The linked list holds the
# binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.
#
#
# Example 1:
#
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
#
#
# Example 2:
#
#
# Input: head = [0]
# Output: 0
#
#
#
# Constraints:
#
#
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
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
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head:
            answer = answer*2 + head.val
            head = head.next
        return answer
# @lc code=end
