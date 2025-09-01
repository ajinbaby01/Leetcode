/*
 * @lc app=leetcode id=144 lang=golang
 *
 * [144] Binary Tree Preorder Traversal
 *
 * https://leetcode.com/problems/binary-tree-preorder-traversal/description/
 *
 * algorithms
 * Easy (69.79%)
 * Likes:    8573
 * Dislikes: 227
 * Total Accepted:    2.2M
 * Total Submissions: 2.9M
 * Testcase Example:  '[1,null,2,3]'
 *
 * Given the root of a binary tree, return the preorder traversal of its nodes'
 * values.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,null,2,3]
 *
 * Output: [1,2,3]
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
 * Output: [1,2,4,5,6,7,3,8,9]
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
 * The number of nodes in the tree is in the range [0, 100].
 * -100 <= Node.val <= 100
 *
 *
 *
 * Follow up: Recursive solution is trivial, could you do it iteratively?
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
func preorderTraversal(root *TreeNode) []int {
	// return recursive(root)
	return iterative(root)
}

func iterative(root *TreeNode) []int {
	var preorder []int
	var stack []*TreeNode
	// As long as you either have nodes left to visit (root != nil) or pending work in the stack (len(stack) > 0), keep looping.
	for root != nil || len(stack) != 0 {
		// Simulates calling dfs(root.left) within dfs(root)
		for root != nil {
			preorder = append(preorder, root.Val)
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		root = root.Right
	}
	return preorder
}

func recursive(root *TreeNode) []int {
	var dfs func(root *TreeNode)
	var preorder []int
	dfs = func(root *TreeNode) {
		if root != nil {
			preorder = append(preorder, root.Val)
			dfs(root.Left)
			dfs(root.Right)
		}
	}
	dfs(root)
	return preorder
}

// @lc code=end
