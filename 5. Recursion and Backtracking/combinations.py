from typing import List


class Solution:
    def combine(self, nums: List, k: int) -> List[List[int]]:
        def recursion(nums, start, comb=[], answer=[]):
            nums.sort()
            if len(comb) == k:
                answer.append(comb[:])

            visited = set()

            for i in range(start, len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    comb.append(nums[i])
                    recursion(nums, i+1, comb)
                    comb.pop()
            return answer
        return recursion(nums, 0)
print(Solution().combine([4,4,4,1,4], 2))
