#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (36.13%)
# Likes:    8996
# Dislikes: 425
# Total Accepted:    598.9K
# Total Submissions: 1.7M
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#   '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
#
#
# Example 1:
#
#
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = False
        self.refs = 0

    def add_word(self, word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.refs += 1
        curr.word = True

    def remove_word(self, word):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.child:
                curr = curr.child[c]
                curr.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        rows = len(board)
        cols = len(board[0])
        res, visit = [], set()
        for w in words:
            root.add_word(w)

        def dfs(row, col, node, word):
            if (
                row not in range(rows) or
                col not in range(cols) or
                board[row][col] not in node.child or
                node.refs == 0 or
                (row, col) in visit
            ):
                    return
            visit.add((row, col))
            node = node.child[board[row][col]]
            word += board[row][col]
            if node.word:
                res.append(word)
                node.word = False
                # Removes the word
                # The object on which function is called is root (not node)
                root.remove_word(word)


            dfs(row - 1, col, node, word)
            dfs(row + 1, col, node, word)
            dfs(row, col - 1, node, word)
            dfs(row, col + 1, node, word)
            visit.remove((row, col))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")

        return res
# @lc code=end
