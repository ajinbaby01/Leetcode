#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (65.99%)
# Likes:    11617
# Dislikes: 248
# Total Accepted:    629.4K
# Total Submissions: 945K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 9
#
#
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # return self.nQueens(n)
        return self.neetCodeNQueens(n)

    def neetCodeNQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]

        column = set()
        left_diag = set()
        right_diag = set()

        def dfs(row):
            if row == n:
                copy = [''.join(r) for r in board]
                res.append(copy)
                return

            for col in range(n):
                if col in column or (row + col) in right_diag or (row - col) in left_diag:
                    continue

                column.add(col)
                right_diag.add(row + col)
                left_diag.add(row - col)
                board[row][col] = 'Q'

                dfs(row + 1)

                column.remove(col)
                right_diag.remove(row + col)
                left_diag.remove(row - col)
                board[row][col] = '.'
                
        dfs(0)
        return res

    def nQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]

        # We start from row, col and go up because the below rows won't be
        # filled until current row is filled
        def isValid(row, col):
            # check col
            i = row
            while i >=0:
                if board[i][col] == 'Q':
                    return False
                i -= 1

            # check left diagonal
            i, j = row, col
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # check right diagonal
            i, j = row, col
            while i>=0 and j<n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def dfs(row):
            if row == n:
                copy = [''.join(r) for r in board]
                res.append(copy)
                return

            for col in range(n):
                if isValid(row, col):
                    board[row][col] = 'Q'
                    dfs(row + 1)
                    board[row][col] = '.'
        dfs(0)
        return res
# @lc code=end
