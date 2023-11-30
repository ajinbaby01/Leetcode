#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (46.30%)
# Likes:    15453
# Dislikes: 629
# Total Accepted:    1.4M
# Total Submissions: 3M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return self.dfsNumCourses(numCourses, prerequisites)
        return self.bfsKahnAlgorithmNumCourses(numCourses, prerequisites)
    
    # Topological Sort from techinterview
    def bfsKahnAlgorithmNumCourses(self, numCourses, prerequisites):
        nodes, order, queue = {}, [], deque()
        for node_id in range(numCourses):
            nodes[node_id] = { 'in': 0, 'out': set() }
        for node_id, pre_id in prerequisites:
            nodes[node_id]['in'] += 1
            nodes[pre_id]['out'].add(node_id)
        for node_id in nodes.keys():
            if nodes[node_id]['in'] == 0:
                queue.append(node_id)
        while len(queue):
            node_id = queue.pop()
            for outgoing_id in nodes[node_id]['out']:
                nodes[outgoing_id]['in'] -= 1
                if nodes[outgoing_id]['in'] == 0:
                    queue.append(outgoing_id)
            order.append(node_id)
        return len(order) == numCourses
    
    def dfsNumCourses(self, numCourses, prerequisites):
        if not prerequisites:
            return True
        
        # adjacency list graph representation of prerequisites
        graph = [[] for _ in range(numCourses)]
        
        # Used to keep the nodes visited on one dfs iteration.
        # When you start dfs at node 0, you add 0 to visited.
        # You dfs through one 0's neighbor say 3, then you add 3 to visited.
        # 3 has a neighbor 5, so you add 5 to visited.
        # But 5 has 0 as neighbor. 0 is present in visited meaning loop is found.
        # If no loop found after dfs though all of 0's children,
        # you need to remove 0 from visited as visited is used to track nodes during 'one' dfs iteration.
        visited = set()
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def dfs(crs):
            # Loop detected (deadlock) so courses cannot be completed
            if crs in visited: 
                return False
            
            # This course has no prerequisites, so we can say the specific course can be completed
            if graph[crs] == []:
                return True
            
            # Add course to visited, so we can detect loop in dfs
            visited.add(crs)
            
            # dfs through the children of current course
            for prereq in graph[crs]:
                # if loop detected
                if not dfs(prereq):
                    return False
            
            # dfs starting from current course is over, so we can remove it from visited
            visited.remove(crs)
            
            # We know that if we reach here, a dfs starting from current course won't find a loop.
            # This node might be a neighbor/prerequisite for some other node.
            # During dfs starting from that node, we will come to this node.
            # Then we can instantly return True as we know from earlier iterations that this course can be completed (ie, no loop includes this node).
            # Setting the prerequisites/neighbors to empty after finding no loops will reduce repetitive work (ie, we won't dfs this node again)
            graph[crs] = []
            
            # This course can be completed, so return True
            return True
            
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
# @lc code=end

