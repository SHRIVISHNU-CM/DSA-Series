def getMinDiff(arr,n,k):
    arr.sort()

    res = arr[-1] -arr[0]

    for i in range(1,n):
        if arr[i] - k<0:
            continue

        min_height = min(arr[0]+k,arr[i]-k)

        max_height = max(arr[i-1] +k , arr[-1] -k)

        res = min(res,max_height-min_height)

    return res

k = 2
n = 4
arr = [1,5,8,10]

print(getMinDiff(arr,n,k))