class Solution:
    def removeDuplicates(self, arr: list) -> list:
        # return self.copyUniqueElements(arr)
        return self.inPlace(arr)

    def copyUniqueElements(self, arr: list) -> list:
        ans = [arr[0]]  # Stores the unique elements
        for i in range(len(arr)):
            if arr[i] != ans[-1]:
                ans.append(arr[i])
        return ans
    # Time: O(n), Space: O(n)

    def inPlace(self, arr: list) -> list:
        j = 0  # points to the previous unique element
        for i in range(1, len(arr)):
            if (
                arr[i] != arr[j]
            ):  # if current element is not equal to previous unique element
                j += 1
                arr[j] = arr[i]
        return arr[: j + 1]
    # Time: O(n), Space: O(1)

print(Solution().removeDuplicates([1, 2, 2, 2, 4, 4, 5, 6]))  # [1, 2, 4, 5, 6]
