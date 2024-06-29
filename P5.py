def Separate(arr,n):
    temp = [0] *n
    index =0

    for i in range(n):
        if arr[i] >=0:
            temp[index] = arr[i]
            index +=1

    for i in range(n):
        if arr[i] <0:
            temp[index] =arr[i]
            index +=1

    for i in range(n):
        arr[i] = temp[i]
    
n = 8
arr =[1,-1,3,2,-7,-5,11,6]
print(Separate(arr,n))
print(arr)