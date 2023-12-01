#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (62.98%)
# Likes:    7990
# Dislikes: 794
# Total Accepted:    819.8K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
#
# You are also given three integers sr, sc, and color. You should perform a
# flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with color.
#
# Return the modified image after performing the flood fill.
#
#
# Example 1:
#
#
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1)
# (i.e., the red pixel), all pixels connected by a path of the same color as
# the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected to the starting pixel.
#
#
# Example 2:
#
#
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made
# to the image.
#
#
#
# Constraints:
#
#
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m
# 0 <= sc < n
#
#
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # return self.dfsFloodFill(image, sr, sc, color)
        return self.bfsFloodFill(image, sr, sc, color)

    def bfsFloodFill(self, image, sr, sc, color):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        rows, cols = len(image), len(image[0])
        q = deque([(sr, sc)])
        while q:
            i, j = q.popleft()
            visited.add((i, j))
            prev_color = image[i][j]
            image[i][j] = color
            for dr, dc in directions:
                next_i, next_j = i + dr, j + dc
                if next_i in range(rows) and next_j in range(cols) and (next_i, next_j) not in visited and image[next_i][next_j] == prev_color:
                    q.append((next_i, next_j))
        return image

    def dfsFloodFill(self, image, sr, sc, color):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        rows, cols = len(image), len(image[0])

        def dfs(i, j, image, prev):
            if (
                i not in range(rows) or
                j not in range(cols) or
                (i, j) in visited or
                image[i][j] != prev
            ):
                return

            visited.add((i, j))
            prev_color = image[i][j]
            image[i][j] = color

            for dr, dc in directions:
                next_i, next_j = i + dr, j + dc
                dfs(next_i, next_j, image, prev_color)
        dfs(sr, sc, image, image[sr][sc])
        return image

# @lc code=end
