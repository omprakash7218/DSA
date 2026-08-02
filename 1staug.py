# Insertion sort 

arr = [3,5,6,4,8,9,7,1]
for i in range(1,len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] >= key:
        arr[j+1]=arr[j]
        j -= 1
    arr[j+1] = key
print(arr)
# Merge sort 
# we'll use recursion in this method

aray = [3,5,6,4,8,9,7,1]
n = len(aray)
def merge_array(left,right):
    res = []
    i,j = 0,0
    n = len(left)
    m = len(right)
    while i < n and j < m:
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1 
    while j < m:
        res.append(right[j])
        j += 1 
    while i < n:
        res.append(left[i])
        i+=1
    return res

left = [1,2,3]
right = [2,5,6,7,8]
print(merge_array(left,right))
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left_arr,right_arr = arr[:mid],arr[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge_array(left,right)
array = [3,5,6,4,8,9,7,1]
print(merge_sort(array))
