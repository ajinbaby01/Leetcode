# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (56.53%)
# Likes:    14747
# Dislikes: 1328
# Total Accepted:    1.6M
# Total Submissions: 2.7M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# Given the heads of two singly linked-lists headA and headB, return the node
# at which the two lists intersect. If the two linked lists have no
# intersection at all, return null.
#
# For example, the following two linked lists begin to intersect at node c1:
#
# The test cases are generated such that there are no cycles anywhere in the
# entire linked structure.
#
# Note that the linked lists must retain their original structure after the
# function returns.
#
# Custom Judge:
#
# The inputs to the judge are given as follows (your program is not given these
# inputs):
#
#
# intersectVal - The value of the node where the intersection occurs. This is 0
# if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head)
# to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head)
# to get to the intersected node.
#
#
# The judge will then create the linked structure based on these inputs and
# pass the two heads, headA and headB to your program. If you correctly return
# the intersected node, then your solution will be accepted.
#
#
# Example 1:
#
#
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as
# [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are
# 3 nodes before the intersected node in B.
# - Note that the intersected node's value is not 1 because the nodes with
# value 1 in A and B (2^nd node in A and 3^rd node in B) are different node
# references. In other words, they point to two different locations in memory,
# while the nodes with value 8 in A and B (3^rd node in A and 4^th node in B)
# point to the same location in memory.
#
#
# Example 2:
#
#
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as
# [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node
# before the intersected node in B.
#
#
# Example 3:
#
#
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it
# reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0,
# while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#
#
#
# Constraints:
#
#
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 10^4
# 1 <= Node.val <= 10^5
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB
# intersect.
#
#
#
# Follow up: Could you write a solution that runs in O(m + n) time and use only
# O(1) memory?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # listA = [1,9,1,2,4], listB = [3,2,4]
        # return self.bruteForce(headA, headB)
        # return self.hashing(headA, headB)
        # return self.differenceInNodeCount(headA, headB)
        return self.twoPointer(headA, headB)

    def twoPointer(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptrA = headA
        ptrB = headB

        while ptrA is not ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        return ptrA
    # Time: O(A + B), Space: O(1)

    def differenceInNodeCount(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        tempHead = headA
        while tempHead is not None:
            tempHead = tempHead.next
            lenA += 1

        lenB = 0
        tempHead = headB
        while tempHead is not None:
            tempHead = tempHead.next
            lenB += 1

        if lenA > lenB:
            while lenA != lenB:
                headA = headA.next
                lenA -= 1
        else:
            while lenB != lenA:
                headB = headB.next
                lenB -= 1

        while headA is not headB:
            headA = headA.next
            headB = headB.next
        return headA
    # Time: O(A + B), Space: O(1)

    def hashing(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_set = dict()
        while headA is not None:
            hash_set[headA] = None
            headA = headA.next

        while headB is not None:
            if headB in hash_set:
                return headB
            headB = headB.next

        return None
    # Time: O(A + B), Space: O(A)

    def bruteForce(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp = headB
        while headA is not None:
            headB = temp
            while headB is not None:
                if headA is headB:
                    return headA
                else:
                    headB = headB.next
            headA = headA.next
        return None
    # Time: O(A*B), Space: O(1)

# @lc code=end
