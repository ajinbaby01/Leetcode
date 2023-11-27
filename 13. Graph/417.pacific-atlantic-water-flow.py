#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (54.73%)
# Likes:    7009
# Dislikes: 1367
# Total Accepted:    415.6K
# Total Submissions: 757.2K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
#
#
# Example 1:
#
#
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans,
# as shown below:
# [0,4]: [0,4] -> Pacific Ocean
# [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean
# [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
# [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
# [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean
# [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean
# [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean
# ⁠      [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the
# Pacific and Atlantic oceans.
#
#
# Example 2:
#
#
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and
# Atlantic oceans.
#
#
#
# Constraints:
#
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
#
#
#

# @lc code=start
class Solution:
    """
    [       Pacific
        [1, 2, 2, 3, 5]
        [3, 2, 3, 4, 4]
Pacific [2, 4, 5, 3, 1] Atlantic
        [6, 7, 1, 4, 5]
        [5, 1, 1, 2, 4]
    ]       Atlantic
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Start from cells near the oceans and perform dfs/bfs search satisfying graph traversal conditions and if next cell height ≥ current cell height.
        # Use two visited set for tracking cells visited through bfs/dfs from cells near pacific and atlantic separately. Take intersection of these two sets and return.

        return self.bfsPacificAtlantic(heights)
        # return self.dfsPacificAtlantic(heights)

    def bfsPacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visitedP = set()
        visitedA = set()

        def bfs(i, j, visited):
            q = deque([(i, j)])
            while q:
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                for dr, dc in directions:
                    next_i, next_j = i + dr, j + dc
                    if (
                        next_i in range(rows) and
                        next_j in range(cols) and
                        heights[next_i][next_j] >= heights[i][j]
                    ):
                        q.append((next_i, next_j))

        for r in range(rows):
            bfs(r, 0, visitedP)
            bfs(r, cols - 1, visitedA)

        for c in range(cols):
            bfs(0, c, visitedP)
            bfs(rows - 1, c, visitedA)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visitedP and (r, c) in visitedA:
                    res.append([r, c])

        return res

    def dfsPacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visitedP = set()
        visitedA = set()

        def dfs(i, j, visited):
            visited.add((i, j))
            for dr, dc in directions:
                next_i, next_j = i + dr, j + dc
                if (
                    next_i in range(rows) and
                    next_j in range(cols) and
                    (next_i, next_j) not in visited and
                    heights[next_i][next_j] >= heights[i][j]
                ):
                    dfs(next_i, next_j, visited)

        for r in range(rows):
            dfs(r, 0, visitedP)
            dfs(r, cols - 1, visitedA)

        for c in range(cols):
            dfs(0, c, visitedP)
            dfs(rows - 1, c, visitedA)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visitedP and (r, c) in visitedA:
                    res.append([r, c])

        return res

# @lc code=end
