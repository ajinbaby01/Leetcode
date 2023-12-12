"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Explanation:
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'

Example 2:
Input: words = ["z","x"]
Output: "zx"
Explanation:
from "z" and "x", we can get 'z' < 'x'

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Example 4:
Input: words = ["a","ba","bc", "c"]
Output: "abc"

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

from collections import defaultdict, deque
from typing import List

# class Node:
#     def __init__(self, val, neighbors=[]):
#         self.val = val
#         self.neighbors = neighbors if neighbors else []

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def build_adjacency_list(words):

            edges = []

            for i in range(len(words) - 1):
                word1 = words[i]
                word2 = words[i + 1]

                for j in range(len(word1)):
                    if word1[j] != word2[j]:
                        edges.append([word1[j], word2[j]])
                        break

            adjacency_list = defaultdict(list)
            for u, v in edges:
                adjacency_list[u].append(v)

            return edges, adjacency_list

        def topological_sort(edges, adjacency_list):
            indegree, order, q, visited = {}, [], deque(), set()

            for u, v in edges:
                indegree[u] = 0
                indegree[v] = 0

            for u, v in edges:
                indegree[v] += 1

            for node, ind in indegree.items():
                if ind == 0:
                    q.append(node)

            while q:
                node = q.popleft()
                visited.add(node)
                order.append(node)
                for neighbor in adjacency_list[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)

            return order

        edges, adjacency_list = build_adjacency_list(words)

        num_nodes = set()
        for u, v in edges:
            num_nodes.add(u)
            num_nodes.add(v)
        num_nodes = len(num_nodes)

        order = topological_sort(edges, adjacency_list)

        return ''.join(order) if len(order) == num_nodes else -1

words = [
    ["wrt","wrf","er","ett","rftt"], # wertf
    ["z","x"], # zx
    ["a","z","x","z"], # -1
    ["a","ba","bc", "c"] # abc
]

for word in words:
    print(Solution().alienOrder(word))
