# Two sum (brute force) O(n^2)
from itsdangerous import want_bytes


nums = [5,1,4,9,2,15,6,3]
target = 13
n = len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j] == target:
            print([i,j])
# remove duplicates from an array
array = [0,0,1,1,1,2,2,3,3,3,4,4,4,5]
l = 1 
for r in range(1,len(array)):
    if array[r]!=array[r-1]:
        array[l]=array[r]
        l+=1
print(l) 
print(array)
# Find missing number from  1 to N using sum formula

lst = [1,2,3,4,5,7,8,9]
def missing_number(lst):
    n = len(lst)+1
    expected_sum = n * (n+1)//2
    actual_sum = sum(lst)
    return expected_sum-actual_sum
print(missing_number(lst))    

# Linear search: return index of target, -1 if not found
# 1st way
lst2 = [10,5,8,3,47]
target = 47
for index,item in enumerate(lst2):
    if item == target:
        print(f"Found at index {index}.")
        break
if target not in lst2:
    print(-1)
# 2nd way 
lst2 = [10,5,8,3,47]
target = 475
index = -1
for item in lst2:
    index += 1
    if item == target:
        print(f"Found at index {index}.")
        break
if target not in lst2:
    print(-1)
# ! right approach is defining a function
lst = [1,21,54,87,564,3218,8741,2]
target = 54
def find_target(lst,target):
    for index,item in enumerate(lst):
        if item == target:
            return index
    return -1
print(find_target(lst,target))

