#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (63.70%)
# Likes:    10993
# Dislikes: 122
# Total Accepted:    914.8K
# Total Submissions: 1.4M
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
#  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
#
# Implement the Trie class:
#
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
#
#
#
# Example 1:
#
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
#
#
#


# @lc code=start
class Node:
    def __init__(self, value=0):
        self.value = value
        self.links = [None] * 26

class TrieUsingLinkedNodes:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        for letter in word:
            if not root.links[ord(letter) - ord("a")]:
                node = Node()
                root.links[ord(letter) - ord("a")] = node
            root = root.links[ord(letter) - ord("a")]
        root.value = 1

    def search(self, word: str) -> bool:
        root = self.root
        for letter in word:
            if not root.links[ord(letter) - ord("a")]:
                return False
            root = root.links[ord(letter) - ord("a")]
        if root.value == 0:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for letter in prefix:
            if not root.links[ord(letter) - ord("a")]:
                return False
            root = root.links[ord(letter) - ord("a")]
        return True

class Trie:
    # Uses dictionary to mimic the links
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]
        trie['word'] = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                return False
            trie = trie[letter]
        return 'word' in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for letter in prefix:
            if letter not in trie:
                return False
            trie = trie[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
