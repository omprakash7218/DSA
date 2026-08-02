# remove duplicates from a sorted array 
array = [1,2,2,4,4,4,5]
freq_map = {}
for i in range(0,len(array)):
    if array[i] not in freq_map:
        freq_map[array[i]] = 1
    else:
        continue
j = 0
for key in freq_map:
    array[j] = key
    j += 1

print(array)

# right rotate an array by 1 place 
ar = [1,2,3,4,5,6]
#without slicing 
def right_rotate(ar):
    last = ar[-1]
    for i in range(len(ar)-2,-1,-1):
        ar[i+1]=ar[i]
    ar[0] = last
    return ar
print(right_rotate(ar))
# using slicing
ary = [0,1,2,3,4,5]
print(ary[::-1])
arr = [0,1,2,3,4,5]
print(arr[-1:]) 
print(arr[:5])
arr = arr[-1:] + arr[:5]
print(arr)
arr = arr[-1:] + arr[:-1]

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
array = [1,2,3,4,5,6,7,8,9,0]
k = 2 
n = len(array)
while k > 0:
    last = array[n-1]
    for i in range(n-2,-1,-1):
        array[i+1] = array[i]
    array[0] = last
    k -= 1
print(array)
