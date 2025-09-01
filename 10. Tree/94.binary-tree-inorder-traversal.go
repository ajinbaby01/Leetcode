/*
 * @lc app=leetcode id=94 lang=golang
 *
 * [94] Binary Tree Inorder Traversal
 *
 * https://leetcode.com/problems/binary-tree-inorder-traversal/description/
 *
 * algorithms
 * Easy (75.57%)
 * Likes:    13295
 * Dislikes: 759
 * Total Accepted:    2.5M
 * Total Submissions: 3.3M
 * Testcase Example:  '[1,null,2,3]'
 *
 * Given the root of a binary tree, return the inorder traversal of its nodes'
 * values.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,null,2,3]
 * Output: [1,3,2]
 *
 *
 * Example 2:
 *
 *
 * Input: root = []
 * Output: []
 *
 *
 * Example 3:
 *
 *
 * Input: root = [1]
 * Output: [1]
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

func inorderTraversal(root *TreeNode) []int {
	// return recursive(root)
	return iterative(root)

}

func iterative(root *TreeNode) []int {
	var stack []*TreeNode
	var inorder []int
	for true {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		if len(stack) == 0 {
			return inorder
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		inorder = append(inorder, root.Val)
		root = root.Right
	}
	return inorder
}

func recursive(root *TreeNode) []int {
	var inorder []int
	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root != nil {
			dfs(root.Left)
			inorder = append(inorder, root.Val)
			dfs(root.Right)
		}
	}
	dfs(root)
	return inorder
}

// @lc code=end
