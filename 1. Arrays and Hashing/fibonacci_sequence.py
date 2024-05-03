from typing import List


class Solution:
    def fibonacci_series_iterative(self, n: int) -> List[int]:
        answer = [0, 1]

        for i in range(n - 2):
            first = answer[i]
            second = answer[i + 1]

            answer.append(first + second)
        return answer

    def fibonacci_series_recursive(self, n: int, answer: List[int] = []) -> List[int]:
        if n <= 1:
            return [0]
        if n == 2:
            return [0, 1]
        answer = self.fibonacci_series_recursive(n - 1)

        answer.append(answer[-1] + answer[-2])

        return answer

    def nth_fibonacci_iterative(self, n: int) -> int:
        first = 0
        second = 1

        for i in range(n - 2):
            answer = first + second
            first = second
            second = answer
        return answer

    def nth_fibonacci_recursive(self, n: int) -> int:
        if n <= 1:
            return 0
        if n == 2:
            return 1
        return self.nth_fibonacci_recursive(n - 1) + self.nth_fibonacci_recursive(n - 2)

    def nth_fibonacci_memoization(self, n: int) -> int:
        # This is same as fibonacci_series_iterative
        if n == 1:
            return 0
        if n == 2:
            return 1
        memo = [None] * (n)
        memo[0] = 0
        memo[1] = 1
        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n - 1]


print(Solution().nth_fibonacci_memoization(18))
