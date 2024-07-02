def maxProfit(arr) :
    if not arr:
        return 0
    
    min_price =float('inf')
    max_profit = 0

    for i in arr:
        min_price = min(min_price,i)
        current_profit = i - min_price
        max_profit = max(max_profit,current_profit)

    return max_profit

arr = [7,1,5,3,6,4]
print(maxProfit(arr))