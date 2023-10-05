from collections import defaultdict
from typing import List


def counting_sort(nums: List[int], k: int):
    n = len(nums)
    count = [0] * k
    output = [0] * n
    for num in nums:
        count[num - 1] += 1
    for i in range(1, k):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        idx = nums[i] - 1
        count[idx] -= 1
        idx = count[idx]
        output[idx] = nums[i]
    return output


# Time: O(n + k), Space: O(k)

print(counting_sort([3, 5, 1, 2, 5, 2, 1], 5))
