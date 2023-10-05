#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (41.61%)
# Likes:    19313
# Dislikes: 870
# Total Accepted:    1.4M
# Total Submissions: 3.4M
# Testcase Example:
# '["LRUCache","put","put","get","put","get","put","get","get","get"]
# '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
#
# Implement the LRUCache class:
#
#
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
#
#
# The functions get and put must each run in O(1) average time complexity.
#
#
# Example 1:
#
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
#
# Constraints:
#
#
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
#
#
#

# @lc code=start
# Hashmap (dict) to keep track of the nodes
# Doubly linked list to keep track of the key-value pairs
# 'put' at the tail
# When using 'get', move the node to tail
# Remove from the head
# Tail node represents the recently used item
# Head node represents the least recently item

# Python's OrderedDict is actually a hashmap with underlying doubly linked list

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def link(self, node1, node2):
        node1.next = node2
        node2.prev = node1

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node()
        self.tail = Node()
        self.link(self.head, self.tail)

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]

        self.link(node.prev, node.next)
        self.link(self.tail.prev, node)
        self.link(node, self.tail)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
            self.dic.pop(key)

        if len(self.dic) == self.capacity:
            node = self.head.next
            self.dic.pop(node.key)
            self._remove(node)

        node = Node(key, value)
        self._add(node)
        self.dic[key] = node

    def _remove(self, node):
        self.link(node.prev, node.next)

    def _add(self, node):
        self.link(self.tail.prev, node)
        self.link(node, self.tail)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end
