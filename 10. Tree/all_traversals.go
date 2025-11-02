// Given the root of a Binary Tree, return the preorder, inorder and postorder traversal sequence of the given tree by making just one traversal.

/*
Each node is tracked with a visit counter that determines which traversal to add it to:​

First Visit (Count = 1)
Add to preorder array (Root → Left → Right pattern). After recording, push the left child onto the stack and increment the counter.​

Second Visit (Count = 2)
Add to inorder array (Left → Root → Right pattern). This happens after returning from the left subtree. Push the right child onto the stack and increment the counter.​

Third Visit (Count = 3)
Add to postorder array (Left → Right → Root pattern). This occurs after both children are fully processed. Pop the node from the stack.​
*/

package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type StackNode struct {
	Node *TreeNode
	// 1 = Preorder, 2 = Inorder, 3 = Postorder
	VisitCount int
}

func main() {
	root := constructComplexTree()
	fmt.Println(allTraversals(root))
	//	Preorder:  [1 2 4 5 7 3 6 8 9]
	// Inorder:   [4 2 7 5 1 3 8 6 9]
	// Postorder: [4 7 5 2 8 9 6 3 1]
}

func allTraversals(root *TreeNode) ([]int, []int, []int) {
	var preorder, inorder, postorder []int

	stack := []StackNode{{root, 1}}
	for len(stack) != 0 {
		top := &stack[len(stack)-1]
		if top.VisitCount == 1 {
			preorder = append(preorder, top.Node.Val)
			top.VisitCount++
			if top.Node.Left != nil {
				stack = append(stack, StackNode{top.Node.Left, 1})
			}
		} else if top.VisitCount == 2 {
			inorder = append(inorder, top.Node.Val)
			top.VisitCount++
			if top.Node.Right != nil {
				stack = append(stack, StackNode{top.Node.Right, 1})
			}
		} else if top.VisitCount == 3 {
			postorder = append(postorder, top.Node.Val)
			stack = stack[:len(stack)-1]
		}
	}
	return preorder, inorder, postorder
}

func constructComplexTree() *TreeNode {
	/*
	       1
	      / \
	     2   3
	    / \   \
	   4   5   6
	      /   / \
	     7   8   9
	*/
	root := &TreeNode{Val: 1}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 3}
	root.Left.Left = &TreeNode{Val: 4}
	root.Left.Right = &TreeNode{Val: 5}
	root.Right.Right = &TreeNode{Val: 6}
	root.Left.Right.Left = &TreeNode{Val: 7}
	root.Right.Right.Left = &TreeNode{Val: 8}
	root.Right.Right.Right = &TreeNode{Val: 9}

	return root
}
