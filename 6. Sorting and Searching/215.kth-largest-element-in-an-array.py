#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (67.14%)
# Likes:    16030
# Dislikes: 765
# Total Accepted:    2M
# Total Submissions: 2.9M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
# Can you solve it without sorting?
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return self.heapFindKthLargest(nums, k)
        # return self.quickSelectFindKthLargest(nums, k)
        return self.betterQuickSelectFindKthLargest(nums, k)

    def betterQuickSelectFindKthLargest(self, nums, k):
        k = len(nums) - k

        def partition(nums):
            pivot = random.choice(nums)
            left = [num for num in nums if num < pivot]
            mid = [num for num in nums if num == pivot]
            right = [num for num in nums if num > pivot]

            return left, mid, right

        def quickSelect(nums, k):
            left, mid, right = partition(nums)

            L, M = len(left), len(mid)

            if L + M <= k:
                return quickSelect(right, k - L - M)
            elif k < L:
                return quickSelect(left, k)
            else:
                return mid[0]

        return quickSelect(nums, k)


    def quickSelectFindKthLargest(self, nums, k):
        k = len(nums) - k

        def partition(l, r):
            p = l
            pivot = nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            return p

        def quickSelect(l, r):
            p = partition(l, r)

            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return quickSelect(l, p - 1)

        return quickSelect(0, len(nums) - 1)
    # Avg Time: O(n), Worst Time: O(n^2), Space: O(1)
    # This solution now TLE because of the last test case

    def heapFindKthLargest(self, nums, k):
        minheap = []

        for num in nums:
            heappush(minheap, num)

            if len(minheap) > k:
                heappop(minheap)

        return heappop(minheap)
    # Time: O(nlogk), Space: O(k)
# @lc code=end
