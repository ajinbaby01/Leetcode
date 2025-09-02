/*
 * @lc app=leetcode id=226 lang=golang
 *
 * [226] Invert Binary Tree
 *
 * https://leetcode.com/problems/invert-binary-tree/description/
 *
 * algorithms
 * Easy (77.16%)
 * Likes:    14758
 * Dislikes: 246
 * Total Accepted:    2.7M
 * Total Submissions: 3.4M
 * Testcase Example:  '[4,2,7,1,3,6,9]'
 *
 * Given the root of a binary tree, invert the tree, and return its root.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [4,2,7,1,3,6,9]
 * Output: [4,7,2,9,6,3,1]
 *
 *
 * Example 2:
 *
 *
 * Input: root = [2,1,3]
 * Output: [2,3,1]
 *
 *
 * Example 3:
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
 * The number of nodes in the tree is in the range [0, 100].
 * -100 <= Node.val <= 100
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package main

func invertTree(root *TreeNode) *TreeNode {
	// return recursiveDFS(root)
	// return iterativeDFS(root)
	return BFS(root)
}

func recursiveDFS(root *TreeNode) *TreeNode {
	if root != nil {
		root.Left, root.Right = root.Right, root.Left
		invertTree(root.Left)
		invertTree(root.Right)
	}
	return root
}

func iterativeDFS(root *TreeNode) *TreeNode {
	var stack []*TreeNode
	head := root
	for root != nil || len(stack) != 0 {
		for root != nil {
			root.Left, root.Right = root.Right, root.Left
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		root = root.Right
	}
	return head
}

func BFS(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	q := []*TreeNode{root}
	for len(q) != 0 {
		node := q[0]
		q = q[1:]
		node.Right, node.Left = node.Left, node.Right
		if node.Right != nil {
			q = append(q, node.Right)
		}
		if node.Left != nil {
			q = append(q, node.Left)
		}
	}
	return root
}

// @lc code=end
