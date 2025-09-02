/*
 * @lc app=leetcode id=110 lang=golang
 *
 * [110] Balanced Binary Tree
 *
 * https://leetcode.com/problems/balanced-binary-tree/description/
 *
 * algorithms
 * Easy (51.11%)
 * Likes:    10530
 * Dislikes: 664
 * Total Accepted:    1.5M
 * Total Submissions: 2.8M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given a binary tree, determine if it is height-balanced.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [3,9,20,null,null,15,7]
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1,2,2,3,3,null,null,4,4]
 * Output: false
 *
 *
 * Example 3:
 *
 *
 * Input: root = []
 * Output: true
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [0, 5000].
 * -10^4 <= Node.val <= 10^4
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
func isBalanced(root *TreeNode) bool {
	// return startFromRoot(root)
	return startFromLeaf(root)
}

// Starts from leaf node
// To start from leaf node, dfs is needed
// Check if bottom subtrees are balanced
// If balanced, return height from both subtrees
// Else return -1 (to indicate false)
func startFromLeaf(root *TreeNode) bool {
	var depth func(root *TreeNode) int
	depth = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left, right := depth(root.Left), depth(root.Right)
		if left == -1 || right == -1 || math.Abs(float64(left - right)) > 1 {
			return -1
		}
		return 1 + max(left, right)
	}
	return depth(root) != -1
}

// Start from root and check if it is balanced
// If root is balanced, check if it's subtree is balanced
func startFromRoot(root *TreeNode) bool {
	if root == nil {
		return true
	}
	diff := math.Abs(float64(depth(root.Left) - depth(root.Right)))
	// root is unbalanced
	if int(diff) > 1 {
		return false
	}
	// if root is balanced, check if both subtrees are balanced
	// because a root can be balanced but the subtree may not be
	return startFromRoot(root.Left) && startFromRoot(root.Right)
}

func depth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return 1 + max(depth(root.Left), depth(root.Right))
}

// @lc code=end
