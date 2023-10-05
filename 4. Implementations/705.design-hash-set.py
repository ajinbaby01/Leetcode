#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (67.18%)
# Likes:    3590
# Dislikes: 289
# Total Accepted:    366.1K
# Total Submissions: 545.1K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
#   '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or
# not.
# void remove(key) Removes the value key in the HashSet. If key does not exist
# in the HashSet, do nothing.
#
#
#
# Example 1:
#
#
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
#
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
#
#
# Constraints:
#
#
# 0 <= key <= 10^6
# At most 10^4 calls will be made to add, remove, and contains.
#
#
#

# @lc code=start
# Using list of lists
# class MyHashSet:
# 	def __init__(self):
# 		self.size = 10000
# 		self.bucket = [[] for _ in range(self.size)]

# 	def add(self, key: int) -> None:
# 		bucket, idx = self._bucket(key)
# 		if idx != -1:
# 			return
# 		bucket.append(key)

# 	def remove(self, key: int) -> None:
# 		bucket, idx = self._bucket(key)
# 		if idx == -1:
# 			return
# 		bucket.remove(key)
# 		# Amortized time complexity of remove() is O(1)
# 		# Since collision occurring is rare,
# 		# the chance of more than one item in a bucket is rare

# 	def contains(self, key: int) -> bool:
# 		bucket, idx = self._bucket(key)
# 		return idx != -1

# 	def _hash(self, key):
# 		return key % self.size

# 	def _bucket(self, key):
# 		hash = self._hash(key)
# 		bucket = self.bucket[hash]
# 		for idx, num in enumerate(bucket):
# 			if num == key:
# 				return bucket, idx
# 		return bucket, -1

##############################################

# Using List of Doubly Linked List
# class ListNode:
# 	def __init__(self, val, nxt, prev) -> None:
# 		self.val = val
# 		self.next = nxt
# 		self.prev = prev

# class MyHashSet:
# 	def __init__(self):
# 		self.size = 19997
# 		self.buckets = [ListNode(-1, None, None) for _ in range(self.size)]

# 	def add(self, key: int) -> None:
# 		bucket = self._bucket(key)
# 		if bucket.val == -1 or bucket.val != key:
# 			node = ListNode(key, None, bucket)
# 			bucket.next = node
# 			return

# 	def remove(self, key: int) -> None:
# 		bucket = self._bucket(key)
# 		if bucket.val == key:
# 			prev = bucket.prev
# 			prev.next = bucket.next
# 			if bucket.next:
# 				bucket.next.prev = prev

# 	def contains(self, key: int) -> bool:
# 		bucket = self._bucket(key)
# 		return bucket.val == key

# 	def _hash(self, key):
# 		return key % self.size

# 	def _bucket(self, key):
# 		hash = self._hash(key)
# 		bucket = self.buckets[hash]
# 		while bucket.next:
# 			if bucket.val == key:
# 				return bucket
# 			bucket = bucket.next
# 		return bucket

##############################################

# Using List of Singly Linked List
# When collision occurs, new node enters at the head instead of tail
# class ListNode:
# 	def __init__(self, val, nxt) -> None:
# 		self.val = val
# 		self.next = nxt

# class MyHashSet:
# 	def __init__(self):
# 		self.size = 19997
# 		self.buckets = [None for _ in range(self.size)]

# 	def add(self, key: int) -> None:
# 		bucket = self._bucket(key)
# 		h = self._hash(key)
# 		if not bucket or bucket.val != key:
# 			node = ListNode(key, self.buckets[h])
# 			# Node is added at head
# 			self.buckets[h] = node

# 	def remove(self, key: int) -> None:
# 		bucket = self._bucket(key)
# 		if bucket:
# 			h = self._hash(key)
# 			node = self.buckets[h]
# 			if node.val == key:
# 				self.buckets[h] = node.next
# 				return
# 			while node.next:
# 				if node.next.val == key:
# 					node.next = node.next.next
# 					return
# 				node = node.next

# 	def contains(self, key: int) -> bool:
# 		bucket = self._bucket(key)
# 		if bucket:
# 			return True
# 		return False

# 	def _hash(self, key):
# 		return key % self.size

# 	def _bucket(self, key):
# 		h = self._hash(key)
# 		bucket = self.buckets[h]
# 		while bucket:
# 			if bucket.val == key:
# 				return bucket
# 			bucket = bucket.next
# 		return bucket

##############################################

# Using List of Singly Linked List of better performance than above
# Removes the key before it is added
# When collision occurs, new node enters at the head instead of tail
class ListNode:
	def __init__(self, val, nxt) -> None:
		self.val = val
		self.next = nxt

class MyHashSet:
	def __init__(self):
		self.size = 19997
		self.buckets = [None for _ in range(self.size)]

	def add(self, key: int) -> None:
		self.remove(key)
		# This is the different line than above method
		h = self._hash(key)
		node = ListNode(key, self.buckets[h])
		# Node is added at head
		self.buckets[h] = node

	def remove(self, key: int) -> None:
		h, node = self._get_node(key)
		if not node:
			return
		if node.val == key:
			self.buckets[h] = node.next
			return
		while node.next:
			if node.next.val == key:
				node.next = node.next.next
				return
			node = node.next

	def contains(self, key: int) -> bool:
		_, node = self._get_node(key)
		while node:
			if node.val == key:
				return True
			node = node.next
		return False

	def _hash(self, key):
		return key % self.size

	def _get_node(self, key):
		h = self._hash(key)
		return h, self.buckets[h]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
