#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.21%)
# Likes:    15985
# Dislikes: 569
# Total Accepted:    1.7M
# Total Submissions: 2.7M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return self.sortedDictionaryMethod(nums, k)
        return self.betterTopKFrequent(nums, k)

    def betterTopKFrequent(self, nums, k):
        # Using the indices of an array to map frequency to num
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        answer = []

        for num in nums:
            count[num] += 1

        for num, fre in count.items():
            freq[fre].append(num)

        for i in range(len(freq) - 1, -1 , -1):
            if freq[i]:
                answer.extend(freq[i])
                if len(answer) == k:
                    return answer
    # Time: O(n), Space: O(n)

    def sortedDictionaryMethod(self, nums, k):
        hm = {}

        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        sorted_hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)

        answer = []
        for i in range(k):
            answer.append(sorted_hm[i][0])

        return answer

    # Time: O(nlogn), Space: O(n)


# @lc code=end
