package main

import "fmt"

func leaders() {
	nums := []int{10, 22, 12, 3, 0, 6}
	n := len(nums)
	var leaders []int
	currentLeader := nums[n - 1]
	leaders = append(leaders, currentLeader)

	for i := n - 2; i > -1; i-- {
		if nums[i] > currentLeader {
			currentLeader = nums[i]
			leaders = append(leaders, nums[i])
		}
	}
	fmt.Println(leaders)
}
