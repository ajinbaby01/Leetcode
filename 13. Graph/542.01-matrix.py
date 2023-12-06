#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (47.57%)
# Likes:    8976
# Dislikes: 395
# Total Accepted:    505.4K
# Total Submissions: 1.1M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
#
# Example 1:
#
#
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
#
#
# Example 2:
#
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#
#
# Constraints:
#
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
#
#
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # return self.slowButWorksTLE(mat)
        return self.singleBFS(mat)

    def singleBFS(self, mat):
        # This works similar to pacific water flow problem
        # Start from 0 cells instead of 1 cells
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(mat), len(mat[0])
        # visited = set()
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                    # visited.add((i, j))
                # This else clause can be used to avoid using visited set
                else:
                    # Marking as not processed
                    mat[i][j] = -1

        while q:
            i, j = q.popleft()
            for dr, dc in directions:
                next_i, next_j = i + dr, j + dc
                if (
                    next_i in range(rows) and
                    next_j in range(cols) and
                    # (next_i, next_j) not in visited

                    # Only add to queue if not processed
                    mat[next_i][next_j] == -1
                ):
                    # visited.add((next_i, next_j))
                    q.append((next_i, next_j))

                    # Value changed from -1 so it is not processed again
                    # If mat[i][j] is 1 away from 0 cell and mat[next_i][next_j] is 1 away from (i,j),
                    # then (i, j) will be 2 away from 0 cell. This is extrapolated for all cells.
                    mat[next_i][next_j] = mat[i][j] + 1

        return mat

    def slowButWorksTLE(self, mat):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(mat), len(mat[0])

        def bfs(i, j):
            visited = set()
            q = deque([(i, j)])
            sr, sc = i, j
            while q:
                i, j = q.popleft()
                visited.add((i, j))
                for dr, dc in directions:
                    next_i, next_j = i + dr, j + dc
                    if (
                        next_i in range(rows) and
                        next_j in range(cols) and
                        (next_i, next_j) not in visited
                    ):
                        if mat[next_i][next_j] == 1:
                            q.append((next_i, next_j))
                        elif mat[next_i][next_j] == 0:
                            return abs(next_i - sr) + abs(next_j - sc)

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    d = bfs(i, j)
                    mat[i][j] = d
        return mat
# @lc code=end
