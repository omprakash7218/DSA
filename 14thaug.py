# remove duplicates from a sorted array

array = [1,1,1,1,2,2,2,3,4,5,6,6,6,6,7,8,10,10,10]
# seen = set()
# seen.add(array[0])
# n = len(array)
# for i in range(1,n-1):
#     for j in range(i+1,n):
#         if array[j] in seen:
#             continue
#         else:
#             seen.add(array[j])
#             array[i],array[j] = array[j],array[i]
#             break
# print(len(seen))        
        
def remove_duplicates(array):
    n = len(array)
    freq_map = {}
    for i in range(n):
        freq_map[array[i]] = 1
    j = 0
    for k in freq_map:
        array[j] = k
        j += 1

    return array,j

print(remove_duplicates(array))

# optimal solution
ar = [1,1,1,2,2,3,4,5,7,7,8,9,9,9,9,10]
i = 0
for j in range(1,len(ar)):
    if ar[j] == ar[i]:
        continue
    else:
        ar[j],ar[i+1] = ar[i+1],ar[j]
        i += 1
print(i+1,ar)

# rotate an array by 1 place
lst = [1,2,3,4,5,6,7,8,9,10]
def rotate(array):
    n = len(array)
    last = array[-1]
    for i in range(n-1,0,-1):
        array[i],array[i-1] = array[i-1],array[i]
    array[0] = last
    return array
print(rotate(lst))

# rotate the array by k elements
# brute force
def rotatek(array,k):
    n = len(array)
    k = k%n
    while k > 0:
        last = array[-1]
        for i in range(n-1,0,-1):
            array[i],array[i-1] = array[i-1],array[i]
        array[0] = last
        k -= 1
    return array
array = [1,2,3,4,5,6,7,8,9]
print(rotatek(array,9))
# optimal or thinking perspective change

def reverse(array,left,right):
    while left < right :
        array[left],array[right] =  array[right],array[left]
        left += 1
        right -= 1
array = [1,2,3,4,5,6,7]
n = len(array)
k = 3
k = k%n 
reverse(array,0,n-1)
reverse(array,k,n-1)
print(array)


# move zeros to the end
ar = [0,1,0,3,12]
for i in range(len(ar)-1):
    if ar[i] == 0:
        for j in range(i+1,len(ar)):
            if ar[j] != 0:
                ar[j],ar[i] = ar[i],ar[j]
                break

print(ar)

print("Here we go!")
ar = [0,1,2]
def move_zero(ar):
    lst = []
    n = len(ar)
    for i in range(n):
        if ar[i] != 0:
            lst.append(ar[i])
        
    j = 0
    for k in lst:
        ar[j] = k
        j+=1
    while j < n:
        ar[j] = 0
        j +=1
    return ar

print(move_zero(ar))


# linear search 
ls = [1,2,3,4,5,5]
def linear_search(array,target): 
    for k in range(len(ls)):
        if ls[k] == target:
            return k
    return -1
    
print(linear_search(ls,8))

a = [1,1,3,5,6,7,12,1,1,1,1,1,1]
b = [2,2,2,2,2,2,12,21,52,64,75,200]
merge_array = []
i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j] or a[i] == b[j]:
        if  len(merge_array) == 0 or merge_array[-1] !=a[i] :
            merge_array.append(a[i])
        i += 1    
    else:
        if len(merge_array) == 0 or b[j] != merge_array[-1]:
            merge_array.append(b[j])
        j += 1
while i < len(a):
    if a[i] != merge_array[-1]:
        merge_array.append(a[i])
    i+=1
while j < len(b):
    if b[j] != merge_array[-1]:
        merge_array.append(b[j])
    j+=1
print(merge_array)

# find the missing number in an array
# using dictionary  using set is already submitted on leetcode