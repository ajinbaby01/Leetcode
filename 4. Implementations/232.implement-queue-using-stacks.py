#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (63.91%)
# Likes:    6711
# Dislikes: 383
# Total Accepted:    734.1K
# Total Submissions: 1.1M
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push,
# peek, pop, and empty).
#
# Implement the MyQueue class:
#
#
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
#
#
# Notes:
#
#
# You must use only standard operations of a stack, which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may
# simulate a stack using a list or deque (double-ended queue) as long as you
# use only a stack's standard operations.
#
#
#
# Example 1:
#
#
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
#
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
#
#
#
# Constraints:
#
#
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
#
#
#
# Follow-up: Can you implement the queue such that each operation is amortized
# O(1) time complexity? In other words, performing n operations will take
# overall O(n) time even if one of those operations may take longer.
#
#

# @lc code=start
class MyQueue:

    # def __init__(self):
    #     self.stack1 = []
    #     self.stack2 = []

    # def push(self, x: int) -> None:
    #     self.stack1.append(x)

    # def pop(self) -> int:
    #     while self.stack1:
    #         item = self.stack1.pop()
    #         self.stack2.append(item)
    #     top = self.stack2.pop()

    #     while self.stack2:
    #         item = self.stack2.pop()
    #         self.stack1.append(item)

    #     return top


    # def peek(self) -> int:
    #     if self.stack1:
    #         return self.stack1[0]

    # def empty(self) -> bool:
    #     return not self.stack1
    # Enqueue(Push): O(1), Dequeue(Pop): O(N)

####################################################################

    # def __init__(self):
    #     self.input = []
    #     self.output = []

    # def push(self, x: int) -> None:
    #     self.input.append(x)

    # def pop(self) -> int:
    #     self.peek()
    #     return self.output.pop()

    # def peek(self) -> int:
    #     if not self.output:
    #         while self.input:
    #             self.output.append(self.input.pop())
    #     return self.output[-1]


    # def empty(self) -> bool:
    #     if self.input or self.output:
    #         return False
    #     return True
    # Enqueue(Push): O(1). Deque(Pop): O(1) amortized
    # https://leetcode.com/problems/implement-queue-using-stacks/solutions/64206/short-o-1-amortized-c-java-ruby/

####################################################################

    # Easier version that modifies the first method
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        # The while loop (O(n)) is only run if stack2 is empty
        # Otherwise pop() takes O(1) amortized
        while self.stack1:
            item = self.stack1.pop()
            self.stack2.append(item)
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            return self.stack1[0]

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        return False
    # Enqueue(Push): O(1). Deque(Pop): O(1) amortized

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
