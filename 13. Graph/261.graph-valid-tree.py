"""
You have a graph of n nodes labeled from 0 to n - 1.
You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

Constraints:
1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
"""


class Solution:
    def valid_tree(self, n, edges):
        # return self.traversal(n, edges)
        return self.findUnion(n, edges)

    def findUnion(self, n, edges):
        par = list(range(n))

        # Find parent of n1
        def find(n1):
            while n1 != par[n1]:
                n1 = par[n1]
            return par[n1]

        for u, v in edges:
            p1, p2 = find(u), find(v)
            if p1 == p2:
                # Cycle Detected
                return False
            # Union without using rank
            par[p1] = p2
            # Decrement component count
            n -= 1
        # Graph is connected/Tree if number of components is 1.
        # Else graph is disconnected (more than one component) and is not a tree.
        return n == 1

    def traversal(self, n, edges):
        # Graph is tree if it is connected and acyclic.
        # Perform dfs.
        # Check for cycles while traversing.
        # After dfs is over, check if number of visited nodes == number of nodes (disconnected)

        if n == 0:
            return True

        def build_adjacency_list(n, edges):
            adjacency_list = [[] for _ in range(n)]
            for u, v in edges:
                adjacency_list[u].append(v)
                adjacency_list[v].append(u)
            return adjacency_list

        adjacency_list = build_adjacency_list(n, edges)
        visited = set()
        # visited.add(0)

        def dfs(node, prev):
            # Add 0 to visited if using the commented dfs.
            # for neighbor in adjacency_list[node]:
            #     if neighbor in visited:
            #         if neighbor != prev:
            #             return False
            #         else:
            #             continue
            #     visited.add(neighbor)
            #     if not dfs(neighbor, node):
            #         return False
            # return True

            # Node visited again = Cycle detected
            if node in visited:
                return False
            visited.add(node)

            for neighbor in adjacency_list[node]:
                # Say there's edges [0, 1] and [1, 0].
                # Start dfs from 0, reach 1
                # Dfs from 1, reach 0 again.
                # If the condition is not used, then when we will again dfs the node from where we came.
                # So we skip the node from where we came from (prev)
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        # return dfs(0, -1) and len(visited) == n

        if dfs(0, -1):
            # If len(visited) != n, then it means it is disconnected.
            # Else it is connected.
            return len(visited) == n
        else:
            # Cycle detected
            return False


n = [5, 5, 5, 6, 5, 5, 6]
edges = [
    [[0, 1], [0, 2], [0, 3], [1, 4]],  # True
    [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],  # False
    [[0, 1], [1, 2], [3, 4], [0, 2]],  # False
    [[1, 5], [0, 2], [2, 4], [4, 2], [2, 0], [5, 1]],  # False
    [[0, 1], [1, 2], [3, 4]],  # False
    [[0, 1], [1, 2], [2, 3], [3, 4]],  # True
    [[0, 5], [0, 2], [5, 2], [2, 4], [1, 3]],  # False
]
for i in range(len(n)):
    print(Solution().valid_tree(n[i], edges[i]))
