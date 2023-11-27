#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (57.74%)
# Likes:    21566
# Dislikes: 470
# Total Accepted:    2.4M
# Total Submissions: 4.1M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Use DFS or BFS traversal on graph.
        # Only continue the traversal if the grid[i][j] == 1.
        # Otherwise return. Update visited each time.
        # When bfs/dfs from one cell/vertex is done, increment count and move to next cell.
        # Repeat for all cells.
        
        # return self.bfsIslands(grid)
        return self.dfsIslands(grid)

    def dfsIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        islands = 0

        def dfs(i, j):
            if (
                (i, j) in visited or
                i not in range(rows) or
                j not in range(cols) or
                grid[i][j] == "0"
            ):
                return

            visited.add((i, j))
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                dfs(next_i, next_j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1

        return islands

    def bfsIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        islands = 0

        def bfs(i, j):
            queue = deque([(i, j)])

            while queue:
                i, j = queue.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                for direction in directions:
                    next_i, next_j = i + direction[0], j + direction[1]
                    if next_i in range(rows) and next_j in range(cols) and grid[next_i][next_j] == "1":
                        queue.append((next_i, next_j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands

# @lc code=end
