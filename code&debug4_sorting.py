from curses import keyname
from os import lstat
import time 


# ! SELECTION SORT 
# selection sort is a algrorithm where we find the next small or large no. and swapping it with the correct position.
lsty = [1,2,3,4,55,4,1,1,2,3,4,5654,2,57,3,1,4,2,3,4,6,3,1,74,8,6,8,8,7,54,8,7,85,14,5,74,84,54]
lst = [3,2,1,5,7,7,8,8]
def selection_sort(lst):
    n = len(lst)
    for l in range(0,n-1):
        for r in range(l+1,n):
            if lst[l]>lst[r]:
                lst[l],lst[r]=lst[r],lst[l]     # kind of bubble sort but not entirely 
    print(lst)
selection_sort(lst)
# seletion sort 
lst = [3,2,1,2]
def selection_sort(lst):
    n = len(lst)
    for l in range(0,n-1):
        min_index = l
        for r in range (l+1,n):
            if lst[min_index]>lst[r]:     # ? using lst[min_index] here makes it dynamic (in my terms)
                min_index = r
        lst[l],lst[min_index] = lst[min_index],lst[l]
    return lst
print(selection_sort(lst))

# Bubble sort 
lst = [3,2,1,2,7,2,5,6,3,2,6,6,7,8,9,567,345,2]
n = len(lst)
for i in range(n-2,-1,-1):
    for j in range(0,n-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
        
print(lst)
# time complexity = T(n2)
# insertion sort 
lst = [5,4,3,2,1,5,6,7,8,9,10]
n = len(lst)
for i in range(0,n-1):
    if lst[i]>lst[i+1]:
        for j in range(i+1,0,-1):
            if lst[j]<lst[j-1]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
print(lst)
# CODE AND DEBUG INSERTION SORT 
lst = [3,5,6,4,8,9,10,7,1]
n = len(lst)
for i in range(0,n):
    if lst[i] > lst[i+1]:
        keys = lst[i+1]
    for j in range(i,-1,-1):
        
        if lst[j]<keys:
            lst[j] = lst[j-1]
        else:
            lst[j]=keys
    
print(lst)
# Merge sort






