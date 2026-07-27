# Today I am learning about "Inplace Modification", "Traversal", "Prefix sum".

# Wht is prefix sum ?  [20,30,59] ----> [20,50,109]
# 1st method
array = [20,50,109]

prefix_sum_array = []
for i in range(len(array)):
	if i == 0:
		prefix_sum_array.append(array[i])
	else:
		prefix_sum_array.append(prefix_sum_array[i-1] + array[i])
print("Prefix Sum Array = ",prefix_sum_array)
# 2nd method

array = [10,12,22]
prefix_sum = []
prefix_sum.append(array[0])

for i in range(1,len(array)):
	prefix_sum.append(prefix_sum[i-1] + array[i])
print("Prefix Sum Array = ",prefix_sum)



# Given an array of numbers, print only the elements at even indices (0, 2, 4, …).
arr = [10, 20, 30, 40, 50]
arr_even=[]
for i in range(len(arr)):
	if i%2 == 0:
		arr_even.append((arr[i]))

print(arr_even)

# I will do inplace modification also brutforce kind of modification
# 1. kind of brute
reverse_array = []
for i in range(len(arr)-1,-1,-1):
	reverse_array.append(arr[i])
print(reverse_array)
#2. inplace modification
ar = [10, 20, 30, 40, 50]
left , right = 0,len(ar)-1
while right>left:
	ar[left],ar[right] = ar[right],ar[left]
	left += 1
	right -= 1
print(ar)