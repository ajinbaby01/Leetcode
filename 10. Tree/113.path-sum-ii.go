/*
 * @lc app=leetcode id=113 lang=golang
 *
 * [113] Path Sum II
 *
 * https://leetcode.com/problems/path-sum-ii/description/
 *
 * algorithms
 * Medium (58.63%)
 * Likes:    8473
 * Dislikes: 168
 * Total Accepted:    1.1M
 * Total Submissions: 1.8M
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
 *
 * Given the root of a binary tree and an integer targetSum, return all
 * root-to-leaf paths where the sum of the node values in the path equals
 * targetSum. Each path should be returned as a list of the node values, not
 * node references.
 *
 * A root-to-leaf path is a path starting from the root and ending at any leaf
 * node. A leaf is a node with no children.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
 * Output: [[5,4,11,2],[5,8,4,5]]
 * Explanation: There are two paths whose sum equals targetSum:
 * 5 + 4 + 11 + 2 = 22
 * 5 + 8 + 4 + 5 = 22
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1,2,3], targetSum = 5
 * Output: []
 *
 *
 * Example 3:
 *
 *
 * Input: root = [1,2], targetSum = 0
 * Output: []
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [0, 5000].
 * -1000 <= Node.val <= 1000
 * -1000 <= targetSum <= 1000
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

func pathSum(root *TreeNode, targetSum int) [][]int {
	var pathSumList [][]int
	var dfs func(root *TreeNode, pathSum int, path []int)
	dfs = func(root *TreeNode, pathSum int, path []int) {
		if root == nil {
			return
		}

		path = append(path, root.Val)
		pathSum += root.Val
		if root.Left == nil && root.Right == nil && pathSum == targetSum {
			// Copy is made because path is a slice and slices are pointers
			// If path is appended to pathSumList and then path is modified in another subtree, the slice inside pathSumList will also get modified
			pathCopy := make([]int, len(path))
			copy(pathCopy, path)
			pathSumList = append(pathSumList, pathCopy)
		}
		dfs(root.Left, pathSum, path)
		dfs(root.Right, pathSum, path)
	}
	dfs(root, 0, []int{})
	return pathSumList
}

// @lc code=end
