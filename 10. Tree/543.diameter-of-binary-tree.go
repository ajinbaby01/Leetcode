/*
 * @lc app=leetcode id=543 lang=golang
 *
 * [543] Diameter of Binary Tree
 *
 * https://leetcode.com/problems/diameter-of-binary-tree/description/
 *
 * algorithms
 * Easy (60.60%)
 * Likes:    15051
 * Dislikes: 1189
 * Total Accepted:    2.2M
 * Total Submissions: 3.4M
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * Given the root of a binary tree, return the length of the diameter of the
 * tree.
 *
 * The diameter of a binary tree is the length of the longest path between any
 * two nodes in a tree. This path may or may not pass through the root.
 *
 * The length of a path between two nodes is represented by the number of edges
 * between them.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,2,3,4,5]
 * Output: 3
 * Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1,2]
 * Output: 1
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [1, 10^4].
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
func diameterOfBinaryTree(root *TreeNode) int {
	// return startFromRoot(root)
	return startFromLeaf(root)
}

func startFromLeaf(root *TreeNode) int {
	maxDiameter := 0
	var depth func(root *TreeNode) int
	depth = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left, right := depth(root.Left), depth(root.Right)
		currDiameter := left + right
		maxDiameter = max(maxDiameter, currDiameter)
		return 1 + max(left, right)
	}
	depth(root)
	return maxDiameter
}

// Starts from root and goes to leaf
// Go through all the nodes
// For each node as root, calculate the diameter through the node
// diameter = sum of max depth of left and right subtree
// Check if current diameter is bigger than max diameter
func startFromRoot(root *TreeNode) int {
	maxDiameter := 0
	var dfs func(root *TreeNode)
	var maxDepth func(root *TreeNode) int
	maxDepth = func(root *TreeNode) int {
		if root != nil {
			return 1 + max(maxDepth(root.Left), maxDepth(root.Right))
		}
		return 0
	}
	dfs = func(root *TreeNode) {
		if root != nil {
			// diameter through node = sum of max depth of left and right subtree
			currentDiameter := maxDepth(root.Left) + maxDepth(root.Right)
			maxDiameter = max(currentDiameter, maxDiameter)
			dfs(root.Left)
			dfs(root.Right)
		}
	}
	dfs(root)
	return maxDiameter
}

// Time: O(n^2)
// @lc code=end
