# find the missing number in an array
# using dictionary  using set is already submitted on leetcode
ar = [1,2,3,4,5,6]
diction = {}
for i in ar:
    diction[i]=1

for i in range(len(ar)+1):
    if i not in diction:
        print(i)

# find the maximum subarray sum
