# Today's topics are:
#     1. Two pointers
#     2. Sliding windows
#     3. Prefix sum applications

# 1. Two pointers

## Q. Move all the zero to the end.
arr = [0,1,2,3,0,1,4,4,0]
non_zero = []
with_zero = []
zero_at_end= []
for i in arr:
    if i != 0:
        non_zero.append(i)
    else: 
        with_zero.append(i)
zero_at_end = non_zero+with_zero
print(zero_at_end)


# Two pointer method 

ar = [1,2,4,0,0,3,0]
l = 0
for r in range(len(ar)-1):
    if ar[r] != 0:
        ar[r],ar[l] = ar[l],ar[r]
        l += 1
print(ar)

## Q. Find pair with target sum. 
array = [2,7,3,4,5,6,2]
target = 9

for i in range(len(array)):
    for j in range(i+1 , len(array)):
        if array[i]+array[j] ==  target:
            print((array[i],array[j]))
            j+=1
    i += 1       

# Two pointer method 
arr = [1, 2, -1, 0, 3, -2]
target = 2

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i] + arr[j] + arr[k] == target:
                print((arr[i], arr[j], arr[k]))
            k += 1
        j+=1
    i+=1


ar = [1,2,0,0,0,0,0,1,1245,45,7,0,0,78]
ar1 = []
for x in ar: 
    if x != 0:
        ar1.append(x)

print(ar1)

ar = [x**1.2 for x in ar if x != 0]
print(ar)