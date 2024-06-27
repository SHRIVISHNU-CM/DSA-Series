def kthSmallest(arr,l,r , k):
    def quickSelect(start,end,k):
        if start == end:
            return arr[start]
        
        pivot = arr[end]

        partition_index = start
        for i in range(start,end):
            if arr[i] <= pivot:
                arr[i],arr[partition_index] = arr[partition_index], arr[i]
                partition_index +=1
        arr[partition_index] , arr[end] = arr[end] , arr[partition_index]

        if k == partition_index - start +1:
            return arr[partition_index]
        elif k<partition_index -start +1:
            return quickSelect(start,partition_index-1,k)
        else:
            return quickSelect(partition_index+1,end,k-(partition_index-start+1))
        
    return quickSelect(l,r,k)


arr = [7 ,10, 4, 20, 15]
k = 4 
l=0 
r=4
print(kthSmallest(arr,l,r,k))