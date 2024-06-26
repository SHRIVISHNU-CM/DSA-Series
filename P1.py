
def reverse_array(arr):
    stack = []

    for ele in arr:
        stack.append(ele)

    for i in range(len(arr)):
        arr[i] = stack.pop()


arr = [1,2,3,4,5,9]

res = reverse_array(arr)
print(arr)