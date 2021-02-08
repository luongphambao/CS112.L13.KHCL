
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] >= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i
def kthSmallest(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)
        if (index - l == k - 1):
            return arr[index]
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)
        return kthSmallest(arr, index + 1, r,
                           k - index + l - 1)
    return -1
n,k=map(int, input().split())
arr=[]
for i in range(0,n):
    arr.append(int(input()))


print(kthSmallest(arr, 0, n - 1, k))

