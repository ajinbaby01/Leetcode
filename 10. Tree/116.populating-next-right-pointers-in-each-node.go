/*
 * @lc app=leetcode id=116 lang=golang
 *
 * [116] Populating Next Right Pointers in Each Node
 *
 * https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
 *
 * algorithms
 * Medium (62.94%)
 * Likes:    10226
 * Dislikes: 319
 * Total Accepted:    1.2M
 * Total Submissions: 1.9M
 * Testcase Example:  '[1,2,3,4,5,6,7]'
 *
 * You are given a perfect binary tree where all leaves are on the same level,
 * and every parent has two children. The binary tree has the following
 * definition:
 *
 *
 * struct Node {
 * ⁠ int val;
 * ⁠ Node *left;
 * ⁠ Node *right;
 * ⁠ Node *next;
 * }
 *
 *
 * Populate each next pointer to point to its next right node. If there is no
 * next right node, the next pointer should be set to NULL.
 *
 * Initially, all next pointers are set to NULL.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,2,3,4,5,6,7]
 * Output: [1,#,2,3,#,4,5,6,7,#]
 * Explanation: Given the above perfect binary tree (Figure A), your function
 * should populate each next pointer to point to its next right node, just like
 * in Figure B. The serialized output is in level order as connected by the
 * next pointers, with '#' signifying the end of each level.
 *
 *
 * Example 2:
 *
 *
 * Input: root = []
 * Output: []
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [0, 2^12 - 1].
 * -1000 <= Node.val <= 1000
 *
 *
 *
 * Follow-up:
 *
 *
 * You may only use constant extra space.
 * The recursive approach is fine. You may assume implicit stack space does not
 * count as extra space for this problem.
 *
 *
 */

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
	// return queue(root)
	return constantSpace(root)
}

func constantSpace(root *Node) *Node {
	curr := root

	// Outer loop current points to the parent
	for curr != nil {
		dummy := &Node{} // dummy node for the next level
		// Tail points to the children
		tail := dummy

		for curr != nil { // Traverse current level
			if curr.Left != nil {
				tail.Next = curr.Left
				tail = tail.Next
			}
			if curr.Right != nil {
				tail.Next = curr.Right
				tail = tail.Next
			}
			curr = curr.Next
		}

		curr = dummy.Next
	}

	return root
}

func queue(root *Node) *Node {
	if root == nil {
        return root
    }
	var q []*Node
	q = append(q, root)
	for len(q) != 0 {
		qLen := len(q)
		for i := range qLen {
			node := q[0]
			q = q[1:]
			if i != qLen-1 {
				node.Next = q[0]
			}
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}
	}

	return root
}
// Space: O(n)
// @lc code=end
