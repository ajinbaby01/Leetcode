#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (63.90%)
# Likes:    18796
# Dislikes: 603
# Total Accepted:    2.8M
# Total Submissions: 4.3M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
#
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return self.storeCount(nums)
        # return self.constantSpace(nums)
        # return self.inBuiltCounter(nums)
        return self.optimalSolution(nums)

    # Moore’s Voting Algorithm:
    def optimalSolution(self, nums: List[int]) -> int:
        # Count of the answer will always exceed the total count of other number.
        # Hence, when count value ultimately reaches 0, it will be because the answer is num.
        # Then it becomes the candidate.
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate
    # Time: O(n), Space: O(1)

    def inBuiltCounter(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return counts.most_common(1)[0][0]
    # Space: O(n)

    def constantSpace(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    # Time: O(nlogn), Space: O(1)

    def storeCount(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 2:
                return num
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        # return max(count, key=count.get)
        # # max_count = 0
        # # for num in count.keys():
        # #     if count[num] > max_count:
        # #         ans = num
        # #         max_count = count[num]
        # # return ans
    # Time: O(n), Space; O(n)


# @lc code=end
