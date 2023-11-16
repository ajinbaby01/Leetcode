#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (40.93%)
# Likes:    14648
# Dislikes: 604
# Total Accepted:    1.4M
# Total Submissions: 3.4M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(i , j, word): 
            if len(word) == 0:
                return True

            if (
                i not in range(rows) or
                j not in range(cols) or
                board[i][j] != word[0]
            ):
                return False
            
            tmp = board[i][j]
            board[i][j] = "#"
            
            res = dfs(i + 1, j, word[1:]) or \
                    dfs(i, j + 1, word[1:]) or \
                    dfs(i - 1, j, word[1:]) or \
                    dfs(i, j - 1, word[1:])

            board[i][j] = tmp
            
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, word):
                    return True
        return False        
# @lc code=end

