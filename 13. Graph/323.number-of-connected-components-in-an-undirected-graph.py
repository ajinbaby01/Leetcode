"""
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
"""

from collections import deque
from typing import (
    List,
)


class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # return self.mySolution(n, edges)
        # return self.trackParent(n, edges)
        return self.disjoinSetFindUnion(n, edges)

    def disjoinSetFindUnion(self, n, edges):
        par = [i for i in range(n)]
        # Keeps the size of each component. Used for optimization. Not required
        rank = [1] * n

        # Find the parent of node n1
        def find(n1):
            res = n1

            # If res is the parent of itself, we reached the top, return res
            while res != par[res]:
                # Path compression optimization
                par[res] = par[par[res]]
                res = par[res]
            return res

        # Combine the sets/components containing n1 and n2 to form one set/component
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # Both nodes have same parent. ie, belong in the same disjoint set/component.
            # Hence no need to decrement component count.
            if p1 == p2:
                return 0

            # Say there's a set with 3 nodes whose parent is 0,
            # and a set with 2 nodes whose parent is 4.
            # Rank of 0 is 3 and rank of 4 is 2.
            # We set the parent of 4 to 0 and set rank of 0 to 5,
            # which means now there's a set/component with 5 nodes who parent is 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return 1

        # Initially there's n components, ie, n disjoint sets
        num_of_components = n
        for u, v in edges:
            # Whenever we combine two sets/components, we decrement count by 1.
            # If the nodes to combine belong to the same component, we don't decrement count.
            num_of_components -= union(u, v)
        return num_of_components

    def trackParent(self, n, edges):
        # n = 6
        # edges = [[1, 5], [0, 2], [2, 4]]
        parent = [i for i in range(n)]
        # [0, 1, 2, 3, 4, 5]

        for u, v in edges:
            # 1st edge : [0, 5, 2, 3, 4, 5]
            # 2nd edge : [2, 5, 2, 3, 4, 5]
            # 3rd/Last edge : [4, 5, 4, 3, 4, 5]
            # 3 different type of values == 3 components
            for i, val in enumerate(parent):
                if val == u:
                    parent[i] = v

        count = set()
        count.update(parent)
        return len(count)

    def mySolution(self, n, edges):
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


n = [5, 6, 5, 5, 6]
edges = [
    [[0, 1], [1, 2], [3, 4], [0, 2]],
    [[1, 5], [0, 2], [2, 4]],
    [[0, 1], [1, 2], [3, 4]],
    [[0, 1], [1, 2], [2, 3], [3, 4]],
    [[0, 5], [0, 2], [5, 2], [2, 4], [1, 3]],
]
for i in range(len(n)):
    print(Solution().count_components(n[i], edges[i]))