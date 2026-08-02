# reverse an array using recursion
def rev(ar,i=0,e=None):
    if e == None:
        e = len(ar)-1

    if i>e:
        return ar
    ar[i],ar[e]=ar[e],ar[i]
    return rev(ar,i + 1 , e - 1)
ar = [1,2,3,4]
print(rev(ar))

# find the largest element in an array
ari = [1,2,3,4,5]
def largest(ar):
    max = 0
    for num in ar :
        if num > max :
            max = num
    return max

print(largest(ari))

# find the second largest element in an array without sorting
def secondlargest(ar):
    lar = 0
    slar = 0
    for num in ar:
        if num > lar:
            slar = lar
            lar = num
    return slar
print(secondlargest(ari))

# check if the array is sorted

def sort(ar):
    for l in range(len(ar)-1):
        if ar[l] > ar[l+1]:
            print("Not sorted")
            return
        else:
            continue
    print("Sorted")
(sort(ari))

# Selection sort algorithm
arr = [3,35,6,1,98,1]
for l in range(len(arr)-1):
    min_index = l
    for r in range(l+1,len(arr)):
        if arr[min_index]>arr[r]:
            min_index = r
    arr[min_index],arr[l] = arr[l],arr[min_index]

print(arr)

# SORT USING SELECTION SORT BUT IN DECREASING ORDER

aru = [2,3,5,61,6,12,6]
for l in range(len(aru)-1):
    max_ind = l
    for j in range(l+1,len(aru)):
        if aru[max_ind]<aru[j]:
            max_ind = j

    aru[max_ind],aru[l] = aru[l],aru[max_ind]
print(aru)

# Bubble sort

arj = [5,1,25,12,7,9,2,3,1,4]
j = len(arj)
while j != 1:
    for i in range(j):
        if arj[i] > arj[j-1]:
            arj[i],arj[j-1]=arj[j-1],arj[i]
    j-=1

print(arj)

# code and debug version of bubble sort
arq = [5,1,25,12,7,9,2,3,1,4]



# insertion sort

