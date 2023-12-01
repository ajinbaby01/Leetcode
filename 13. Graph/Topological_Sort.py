import collections

def build_adjacency_list(num_nodes, edge_list):
    adjacency_list = [[] for _ in range(num_nodes)]
    for u, v in edge_list:
        adjacency_list[u].append(v)
    return adjacency_list

def topological_sort_on_adjacency_list(num_nodes, edge_list):
    adjacency_list = build_adjacency_list(num_nodes, edge_list)

    indegree, order, q = [0] * num_nodes, [], collections.deque()

    for u, v in edge_list:
        indegree[v] += 1

    for i, ind in enumerate(indegree):
        if ind == 0:
            q.append(i)

    while q:
        node = q.popleft()
        order.append(node)
        for neighbor in adjacency_list[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return order if len(order) == num_nodes else None

def topological_sort_on_edge_list(num_nodes, edge_list):
    nodes, order, q = {}, [], collections.deque()

    for node_id in range(num_nodes):
        nodes[node_id] = {'in' : 0, 'out' : set()}

    for start, end in edge_list:
        nodes[end]['in'] += 1
        nodes[start]['out'].add(end)

    for node_id in nodes.keys():
        if nodes[node_id]['in'] == 0:
            q.append(node_id)

    while q:
        node_id = q.popleft()
        order.append(node_id)

        for outgoing_id in nodes[node_id]['out']:
            nodes[outgoing_id]['in'] -= 1
            if nodes[outgoing_id]['in'] == 0:
                q.append(outgoing_id)

    return order if len(order) == num_nodes else None

edge_list = [[5, 0], [4, 0], [4, 1], [5, 2], [2, 3], [3, 1]]
num_nodes = 6

print(topological_sort_on_adjacency_list(num_nodes, edge_list))
print(topological_sort_on_edge_list(num_nodes, edge_list))
