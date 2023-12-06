'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2

Example 2
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

from collections import deque
from typing import (
    List,
)

class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        return self.my_solution(n, edges)

    def my_solution(self, n, edges):
        def build_adjacency_list(n, edges):
            adjacency_list = [[] for _ in range(n)]
            for u, v in edges:
                adjacency_list[u].append(v)
            return adjacency_list

        adjacency_list = build_adjacency_list(n, edges)
        not_visited = set()
        not_visited.update(range(n))
        q = deque()
        count = 0

        while len(not_visited) != 0:
            node = not_visited.pop()
            q.append(node)
            while q:
                node = q.popleft()
                if node in not_visited:
                    not_visited.remove(node)
                q.extend(adjacency_list[node])
            count += 1
        return count
    # Time: O(E + V)

n = 6
edges = [[1, 5], [0, 2], [2, 4]]
print(Solution().count_components(n, edges))
