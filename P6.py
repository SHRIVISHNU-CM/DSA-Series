def maxSubArr(arr):
    max_s0_far = float('-inf')
    max_end = 0

    for num in arr:
        max_end = max(num,max_end+num)
        max_s0_far = max(max_s0_far,max_end)

    return max_s0_far


arr = [1,2,3,-2,5]

print(maxSubArr(arr))