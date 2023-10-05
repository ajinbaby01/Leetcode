def merge_sort(arr, left, right):
    if left == right:
        return
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)
    return arr

def merge(arr, left, mid, right):
    i, j = left, mid + 1
    temp = []

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    temp.extend(arr[i:mid+1])
    temp.extend(arr[j:right+1])

    # arr[left:right+1] = temp[::]
    # No need to make a copy of temp (temp[::])
    # In each iteration, temp = [] line creates a new list object
    arr[left:right+1] = temp

    # while i <= mid:
    #     temp.append(arr[i])
    #     i += 1
    # while j <= right:
    #     temp.append(arr[j])
    #     j += 1

    # for i in range(left, right + 1):
    #     arr[i] = temp[i - left]

print(merge_sort([6,5,3,1,8,7,2,4], 0, 7))
