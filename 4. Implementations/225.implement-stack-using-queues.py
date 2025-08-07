#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (62.11%)
# Likes:    5618
# Dislikes: 1155
# Total Accepted:    575.9K
# Total Submissions: 925K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal stack (push,
# top, pop, and empty).
#
# Implement the MyStack class:
#
#
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
#
#
# Notes:
#
#
# You must use only standard operations of a queue, which means that only push
# to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may
# simulate a queue using a list or deque (double-ended queue) as long as you
# use only a queue's standard operations.
#
#
#
# Example 1:
#
#
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
#
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
#
#
#
# Constraints:
#
#
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
#
#
#
# Follow-up: Can you implement the stack using only one queue?
#
#

# @lc code=start
class MyStack:
    # def __init__(self):
    #     self.queue = collections.deque()

    # def push(self, x: int) -> None:
    #     self.queue.append(x)
    #     for _ in range(len(self.queue) - 1):
    #         self.queue.append(self.queue.popleft())

    # def pop(self) -> int:
    #     return self.queue.popleft()

    # def top(self) -> int:
    #     return self.queue[0]

    # def empty(self) -> bool:
    #     return not self.queue

    # Single queue. O(N) for push, O(1) for pop

    # For deque, here, the only allowed operations are popleft() as dequeue
    # and append() as enqueue
    # We assume, enqueue is done at the right (Rear) and dequeue is done at
    # left (Front)

    def __init__(self):
        self.queue = None

    def push(self, x: int) -> None:
        q = collections.deque()
        q.append(x)
        q.append(self.queue)
        self.queue = q

    def pop(self) -> int:
        item = self.queue.popleft()
        self.queue = self.queue.popleft()
        return item

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue

    # O(1) for both push and pop


# Golang
# import (
# 	"container/list"
# 	"fmt"
# )

# // MyStack implements a LIFO stack using one FIFO queue.
# type MyStack struct {
# 	q *list.List // underlying queue
# }

# /* ---------- core operations ---------- */

# // Push adds x to the stack (costly: O(n))
# func (s *MyStack) Push(x int) {
# 	s.q.PushBack(x)              // enqueue new element
# 	for i := 0; i < s.q.Len()-1; i++ { // rotate previous elements
# 		front := s.q.Front()
# 		s.q.Remove(front)
# 		s.q.PushBack(front.Value)
# 	}
# }

# // Pop removes-and-returns the top element (amortized O(1))
# func (s *MyStack) Pop() int {
# 	front := s.q.Front()
# 	s.q.Remove(front)
# 	return front.Value.(int)
# }

# // Top returns, but does not remove, the current top (O(1))
# func (s *MyStack) Top() int {
# 	return s.q.Front().Value.(int)
# }

# // Empty reports whether the stack has no elements (O(1))
# func (s *MyStack) Empty() bool {
# 	return s.q.Len() == 0
# }

# /* ---------- demo ---------- */
# func NewStack() *MyStack { return &MyStack{q: list.New()} }

# func main() {
# 	st := NewStack()
# 	st.Push(10)
# 	st.Push(20)
# 	st.Push(30) // stack = [30 20 10]

# 	fmt.Println(st.Top()) // 30
# 	fmt.Println(st.Pop()) // 30
# 	fmt.Println(st.Top()) // 20
# 	fmt.Println(st.Empty()) // false
# }

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
