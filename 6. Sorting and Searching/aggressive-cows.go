/*
Problem Statement: You are given an array 'arr' of size 'n' which denotes the position of stalls.
You are also given an integer 'k' which denotes the number of aggressive cows.
You are given the task of assigning stalls to 'k' cows (each stall contain one cow) such that the minimum distance between any two of them is the maximum possible.
Find the maximum possible minimum distance.

Example 1:
Input Format: N = 6, k = 4, arr[] = {0,3,4,7,10,9}
Result: 3
Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

Example 2:
Input Format: N = 5, k = 2, arr[] = {4,2,1,3,6}
Result: 5
Explanation: The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions {1, 6}.
*/

package main

import (
	"fmt"
	"slices"
)

func main() {
	fmt.Println(aggressiveCows([]int{0, 3, 4, 7, 10, 9}, 4))
}

/*
Our objective is to find the maximum distance d such that the cows can be placed in the stall
We see that, d is in the range [1, max(stalls[])-min(stalls[])] where we can apply binary search
*/
func aggressiveCows(stalls []int, k int) int {
	slices.Sort(stalls)
	left, right := 1, slices.Max(stalls)-slices.Min(stalls)
	for left <= right {
		mid := left + (right-left)/2
		if countCows(stalls, mid) < k { // k cows cannot be placed, hence reduce the distance
			right = mid - 1
		} else { // k or more than k cows can be placed, hence increase the distance
			left = mid + 1
		}
	}
	return right // right is returned because we are looking for max not min
}

func countCows(stalls []int, dist int) int {
	cows, last := 1, stalls[0]
	for i := 1; i < len(stalls); i++ {
		if stalls[i]-last >= dist {
			cows++
			last = stalls[i]
		}
	}
	return cows
}
