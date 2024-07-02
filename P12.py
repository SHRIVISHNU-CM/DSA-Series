def SubArr(arr,n):
    cumulative_sum = 0
    sum_set = set()

    for num in arr:
        cumulative_sum +=num

        if cumulative_sum ==0 or cumulative_sum in sum_set:
            return True
        
        sum_set.add(cumulative_sum)

    return False

n = 5
arr = [4,2,-3,1,6]
print(SubArr(arr,n))