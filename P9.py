def maxSubArrSum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum = max(num,current_sum +num)
        max_sum = max(current_sum,max_sum)
    return max_sum

arr = [1,2,3,-2,5]
print(maxSubArrSum(arr))