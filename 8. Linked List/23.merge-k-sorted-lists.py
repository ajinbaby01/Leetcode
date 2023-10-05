#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (50.82%)
# Likes:    18395
# Dislikes: 658
# Total Accepted:    1.8M
# Total Submissions: 3.4M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
# Example 1:
#
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
#
# Example 2:
#
#
# Input: lists = []
# Output: []
#
#
# Example 3:
#
#
# Input: lists = [[]]
# Output: []
#
#
#
# Constraints:
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # return self.mergeTwoListsMethod(lists)
        # return self.sortOneListMethod(lists)
        return self.mergeSortListsMethod(lists)

    def mergeSortListsMethod(self, lists):
        # Form pairs of lists. Merge each pair to form sorted list. Repeat for all the pairs
        def mergeTwoLists(list1, list2):
            dummy = head = ListNode()
            while list1 and list2:
                if list1.val <= list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            head.next = list1 or list2
            return dummy.next

        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        mergedList = []

        while len(lists) > 1: # O(logk) because len(lists) gets halved each time
            # Clearing existing list instead of creating a new one in each iteration
            mergedList[:] = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                # mergeTwoLists() takes O(n), n = len(list1) + len(list2)
                mergedList.append(mergeTwoLists(list1, list2))
            # Each time below line is run, a copy of 'lists' is left in memory
            # And 'lists' point to a new list (mergedList)
            # That increases memory usage
            # lists = mergedList

            # Below line overwrites the original copy of 'lists'
            # So that there is no orphaned list in memory
            lists[:] = mergedList
        return lists[0]
    # Time: O(Nlogk), Space: O(logk), N = total number of nodes

    def sortOneListMethod(self, lists):
    # Combine all the lists into 1 long list
    # Sort the combined list
        def getMid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def mergeSort(head):
            if not head or not head.next:
                return head

            left = head
            right = getMid(head)
            tmp = right.next
            right.next = None
            right = tmp

            left = mergeSort(left)
            right = mergeSort(right)
            return merge(left, right)

        def merge(left, right):
            answer = head = ListNode()
            while left and right:
                if left.val <= right.val:
                    head.next = left
                    left = left.next
                else:
                    head.next = right
                    right = right.next
                head = head.next
            head.next = left or right
            return answer.next

        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        dummy = head = ListNode()
        for i in range(k - 1):
            head.next = lists[i]
            while head.next:
                head = head.next
            head.next = lists[i+1]
        return mergeSort(dummy.next)
    # Time: O(NlogN), Space: O(logN), N = number of total nodes
    # Space is O(logN) instead of O(N) because we are sorting nodes and not array
    # O(logN) comes from the recursion stack size
    # Since we recurse logN times, size is O(logN)

    def mergeTwoListsMethod(self, lists):
        # Run 'merge two sorted linked list' algorithm on k lists
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        for i in range(k - 1): # O(k)
            dummy = head = ListNode()
            list1 = lists[i]
            list2 = lists[i+1]
            while list1 and list2: # O(n), n = length of longest list
            # Eg: list1 = 1->2->3->None
            #     list2 = 1->4->None
            #     You iterate through all elements in list1
                if list1.val <= list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            head.next = list1 or list2
            lists[i+1] = dummy.next
            # After merging two lists, in the next iteration, the bigger
            # list is used for comparison, ie, 'n' grows in each iteration
        return lists[i+1]
        # Time: O(Nk), Space: O(1), N = total number of nodes
# @lc code=end
