/*
 * @lc app=leetcode id=49 lang=golang
 *
 * [49] Group Anagrams
 *
 * https://leetcode.com/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (67.37%)
 * Likes:    18925
 * Dislikes: 602
 * Total Accepted:    2.8M
 * Total Submissions: 4.2M
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * Given an array of strings strs, group the anagrams together. You can return
 * the answer in any order.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a
 * different word or phrase, typically using all the original letters exactly
 * once.
 *
 *
 * Example 1:
 * Input: strs = ["eat","tea","tan","ate","nat","bat"]
 * Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
 * Example 2:
 * Input: strs = [""]
 * Output: [[""]]
 * Example 3:
 * Input: strs = ["a"]
 * Output: [["a"]]
 *
 *
 * Constraints:
 *
 *
 * 1 <= strs.length <= 10^4
 * 0 <= strs[i].length <= 100
 * strs[i] consists of lowercase English letters.
 *
 *
 */

// @lc code=start
func groupAnagrams(strs []string) [][]string {
	// return groupByHash(strs)
    return countingFrequency(strs)
}

func countingFrequency(strs []string) [][]string {
    countMap := make(map[[26]int][]string)
    for _, s := range strs {
        var count [26]int
        for _, c := range s {
            count[c - 'a']++
        }
        countMap[count] = append(countMap[count], s)
    }
    groups := make([][]string, 0, len(countMap))
	for _, v := range countMap {
		groups = append(groups, v)
	}
	return groups
}

func groupByHash(strs []string) [][]string {
	hashMap := make(map[uint32][]string)
	hashFn := func(s string) uint32 {
		h := fnv.New32a()
		h.Write([]byte(s))
		return h.Sum32()
	}
	for _, s := range strs {
		splitStr := strings.Split(s, "")
        sort.Strings(splitStr)
        tempStr := strings.Join(splitStr, "")
		strHash := hashFn(tempStr)
		hashMap[strHash] = append(hashMap[strHash], s)
	}
	groups := make([][]string, 0, len(hashMap))
	for _, v := range hashMap {
		groups = append(groups, v)
	}
	return groups
}

// @lc code=end
