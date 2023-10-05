def merge_sort(arr, left, right):
    if left == right:
        return
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    global answer
    i, j = left, mid + 1
    temp = []

    while i <= mid and j <= right:
        if arr[i] > arr[j] + 10:
            temp.append(arr[j])
            j += 1
            answer += 1
        else:
            temp.append(arr[i])
            i += 1

    temp.extend(arr[i:mid+1])
    temp.extend(arr[j:right+1])
    arr[left:right+1] = temp[::]


answer = 0
input = [5,3,8,20,1,5,40,2,1,100]
n = len(input) - 1
merge_sort(input, 0, n)
print(answer)
