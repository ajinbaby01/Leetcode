"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
Return the minimum number of steps needed to move the knight to the square [x, y].
"""

from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Consider the chess board as a matrix.
        # Then perform graph traversal but instead of moving 4-directionally,
        # move how the knight is allowed to moves.
        directions = [
            (-2, 1),
            (-1, 2),
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, -2),
            (-2, -1),
        ]
        q = deque([(0, 0)])
        visited = set()
        moves = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                visited.add((i, j))
                if (i, j) == (x, y):
                    return moves
                for dr, dc in directions:
                    next_i, next_j = i + dr, j + dc
                    if (next_i, next_j) not in visited:
                        q.append((next_i, next_j))
            moves += 1


coords = [(2, 1), (5, 5), (1, -1), (1, 1), (1, 0), (12, 5), (5, 12)]
for x, y in coords:
    moves = Solution().minKnightMoves(x, y)
    print(f"x = {x}, y = {y}, moves = {moves}")
