/*
 * @lc app=leetcode id=104 lang=golang
 *
 * [104] Maximum Depth of Binary Tree
 *
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
 *
 * algorithms
 * Easy (75.52%)
 * Likes:    13748
 * Dislikes: 271
 * Total Accepted:    4.2M
 * Total Submissions: 5.4M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given the root of a binary tree, return its maximum depth.
 *
 * A binary tree's maximum depth is the number of nodes along the longest path
 * from the root node down to the farthest leaf node.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [3,9,20,null,null,15,7]
 * Output: 3
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1,null,2]
 * Output: 2
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [0, 10^4].
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
func maxDepth(root *TreeNode) int {
	// return recursiveDFS(root)
	// return iterativeDFS(root)
	return iterativeBFS(root)
}

func iterativeBFS(root *TreeNode) int {
	if root == nil {
		return 0
	}

	q := []*TreeNode{root}
	depth := 0
	for len(q) != 0 {
		qLen := len(q)
		for range qLen {
			node := q[0]
			q = q[1:]
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}
		// Increment depth every time a level is iterated
		depth++
	}
	return depth
}

func iterativeDFS(root *TreeNode) int {
	if root == nil {
		return 0
	}
	type NodeDepth struct {
		Node  *TreeNode
		Depth int
	}
	stack := []NodeDepth{{
		Node:  root,
		Depth: 1,
	}}
	maxDepth := 0
	for len(stack) != 0 {
		nodeDepth := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		maxDepth = max(maxDepth, nodeDepth.Depth)
		if nodeDepth.Node.Left != nil {
			stack = append(stack, NodeDepth{
				Node:  nodeDepth.Node.Left,
				Depth: nodeDepth.Depth + 1,
			})
		}
		if nodeDepth.Node.Right != nil {
			stack = append(stack, NodeDepth{
				Node:  nodeDepth.Node.Right,
				Depth: nodeDepth.Depth + 1,
			})
		}
	}
	return maxDepth
}

func recursiveDFS(root *TreeNode) int {
	if root != nil {
		return 1 + max(recursiveDFS(root.Left), recursiveDFS(root.Right))
	}
	return 0

	// if root == nil {
	// 	return 0
	// }
	// maxDepth := 0
	// var dfs func(root *TreeNode, depth int)
	// dfs = func(root *TreeNode, depth int) {
	// 	if root != nil {
	// 		maxDepth = max(maxDepth, depth)
	// 		dfs(root.Left, depth + 1)
	// 		dfs(root.Right, depth + 1)
	// 	}
	// }
	// dfs(root, 1)
	// return maxDepth
}

// @lc code=end
