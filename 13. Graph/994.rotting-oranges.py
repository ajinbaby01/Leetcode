#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (53.47%)
# Likes:    12007
# Dislikes: 372
# Total Accepted:    729K
# Total Submissions: 1.4M
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
#
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
#
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        # Until all rotten oranges are processed or if there are no fresh oranges
        while q and fresh > 0:
            # This for loop is used so that when all current rotten oranges
            # are finished, increment minutes by 1.
            # If len(q) is 2, the for loop runs only 2 times,
            # even though we append values to q inside the for loop.
            # The range value is updated only in each while loop.
            for _ in range(len(q)):
                i, j = q.popleft()
                for dr, dc, in directions:
                    next_i, next_j = i + dr, j + dc
                    if (
                        next_i in range(rows) and
                        next_j in range(cols) and
                        (next_i, next_j) not in visited and
                        grid[next_i][next_j] == 1
                    ):
                        fresh -= 1
                        visited.add((next_i, next_j))
                        q.append((next_i, next_j))
            minutes += 1

        if fresh != 0:
            return -1
        else:
            return minutes

# @lc code=end
