/*
 * @lc app=leetcode id=145 lang=golang
 *
 * [145] Binary Tree Postorder Traversal
 *
 * https://leetcode.com/problems/binary-tree-postorder-traversal/description/
 *
 * algorithms
 * Easy (71.26%)
 * Likes:    7542
 * Dislikes: 222
 * Total Accepted:    1.7M
 * Total Submissions: 2.3M
 * Testcase Example:  '[1,null,2,3]'
 *
 * Given the root of a binary tree, return the postorder traversal of its
 * nodes' values.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,null,2,3]
 *
 * Output: [3,2,1]
 *
 * Explanation:
 *
 *
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
 *
 * Output: [4,6,7,5,2,9,8,3,1]
 *
 * Explanation:
 *
 *
 *
 *
 * Example 3:
 *
 *
 * Input: root = []
 *
 * Output: []
 *
 *
 * Example 4:
 *
 *
 * Input: root = [1]
 *
 * Output: [1]
 *
 *
 *
 * Constraints:
 *
 *
 * The number of the nodes in the tree is in the range [0, 100].
 * -100 <= Node.val <= 100
 *
 *
 *
 * Follow up: Recursive solution is trivial, could you do it iteratively?
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

func postorderTraversal(root *TreeNode) []int {
	// return recursive(root)
	return iterative(root)
}

func iterative(root *TreeNode) []int {
	var postorder []int
	var stack []*TreeNode
	// Tracks the most recently processed node to determine if a right subtree has already been visited
	var lastVisited *TreeNode

	for root != nil || len(stack) != 0 {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		// Peek if the node has an unvisited right subtree
		// If so visit it first (left -> right -> root)
		// Not going to actually pop the node because we need to visit it after visiting right subtree
		peekNode := stack[len(stack)-1]
		if peekNode.Right != nil && lastVisited != peekNode.Right {
			root = peekNode.Right
		} else {
			// No right subtree or right subtree is already visited
			// We can visit the node now
			postorder = append(postorder, peekNode.Val)
			stack = stack[:len(stack)-1]
			lastVisited = peekNode
		}
	}

	return postorder
}

func recursive(root *TreeNode) []int {
	var dfs func(root *TreeNode)
	var postorder []int

	dfs = func(root *TreeNode) {
		if root != nil {
			dfs(root.Left)
			dfs(root.Right)
			postorder = append(postorder, root.Val)
		}
	}
	dfs(root)
	return postorder
}

// @lc code=end
