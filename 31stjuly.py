# 31st july , insertion sort
# Bubble sort code n debug version

nums = [1,2,3,4,23,2]
n = len(nums)
sorty = True
def sort(nums):
    n = len(nums)
    sorty = True
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>=nums[j+1] :
                nums[j],nums[j+1]=nums[j+1],nums[j]
                sorty = False
        if sorty == True:
            print("Already sorted")
            return
sort(nums)






nums = [3,5,6,4,8,9,10,7,1]
for i in range(len(nums)-2,-1,-1):
	for j in range(0,i+1):
		if nums[j]>nums[j+1]:
			nums[j],nums[j+1] = nums[j+1],nums[j]

print(nums)



# check if the array is sorted
num1 = [1,2,3,4,5]

def check_sorted(lst):
    sort = True
    for i in range(1,len(lst)):
        if lst[i]< lst[i-1]:
            sort = False
    if sort == True:
        print("It's a sorted array!")
    else:
        print("Oh! not a sorted array")
check_sorted(nums)

# Remove duplicates from a sorted array

num2 = [1,2,2,3,4,5,5,6]
