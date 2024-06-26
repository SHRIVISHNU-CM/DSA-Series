def getMinMax(arr,n):
    if n == 0:
        return
    
    min_val = arr[0]
    max_val = arr[0]

    for i in range(1,n):
        if arr[i] <min_val:
            min_val = arr[i]

        if arr[i]>max_val:
            max_val= arr[i]
    return [min_val,max_val]

arr = [2,3,1,56,1000,8056,167]
n = 7
print(getMinMax(arr,n))