# Move zeros to the end of the array 
# ar = [0,0,0,0,0,0,1]
# for i in range(len(ar)):
#     if ar[i] == 0:
#         k = i 
#         j = i + 1
#         while j < len(ar):
#             if ar[j] == 0:
#                 j+=1
#             else:
#                 ar[k],ar[j] = ar[j],ar[k]
#                 j+=1
# print(ar)

# largest element is the array 

ar = [14,2,2,23,4,54,545,4]
# method1? 
def largest(ar):
    largest = ar[0]
    for nums in ar:
        if nums > largest :
            largest = nums
    return largest

print(largest(ar))

# method2?
def largest2(ar):
    largest = float("-inf")    # method2
    for i in range(len(ar)):
        largest = max(largest,ar[i])
    return largest
print(largest2(ar))

# Second largest number in an array
array = [2,1]
def second_largest(array):
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(len(array)):
        if array[i] > largest :
            second_largest = largest
            largest = array[i]
        elif array[i] > second_largest and array[i] != largest:
            second_largest = array[i]
    return second_largest

print(second_largest(array))

# check if an array is sorted
nums = [3,5,6,8,9,0,20]
def check(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            return False
    return True
print(check(nums))


# recursion
# factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(8))


# check if the array is sorted or not
def check_sort(ar):
    for i in range(len(ar)-1):
        if ar[i] > ar[i+1]:
            return False
    return True

print(check_sort([1,2,4,3,6]))