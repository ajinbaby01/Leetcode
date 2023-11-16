from typing import List


class Solution:
    def combine(self, nums: List, k: int) -> List[List[int]]:
        nums.sort()
        def recursion(nums, comb=[], answer=[]):
            if len(comb) == k:
                answer.append(comb[:])
                return

            visited = set()

            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    comb.append(nums[i])
                    recursion(nums[i+1:])
                    comb.pop()
            return answer
        return recursion(nums)
print(Solution().combine([4,4,4,1,4], 2))
