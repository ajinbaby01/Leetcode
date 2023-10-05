def removeDuplicates(arr):
    j = 0 # points to the previous unique element
    for i in range(1, len(arr)):
        if arr[i] != arr[j]: # if current element is not equal to previous unique element
            j += 1
            arr[j] = arr[i]
    return arr[:j+1]
#Time: O(n), Space: O(1)

print(removeDuplicates([1,2,2,2,4,4,5,6]))
