# Return the numbers that are non-unique (repeating) from the given array
# Length of nums is n
# Numbers are 1 to n

nums = [2,1,6,4,1,2]

result = set()

#############################################
nums.sort()
for i in range(len(nums) - 1):
    if nums[i] < nums[i+1]:
        continue
    result.add(nums[i])
print(result)
# Time: O(nlogn), Space: O(1)
#############################################

#############################################
answer = set()
for num in nums:
    if num not in result:
        result.add(num)
    else:
        answer.add(num)
print(answer)
# Time: O(n), Space: O(n)
#############################################

#############################################
result = set()
for num in nums:
    num = abs(num)
    if nums[num - 1] < 0:
        result.add(num)
    else:
        nums[num - 1] = -nums[num - 1]
print(result)
# Time: O(n), Space: O(1)
#############################################
