#1 max element in unsorted array - track current max variable

from math import inf


lst1 = [1,2,45,555,558,64984,464894]

def find_max(lst):
    if len(lst)==0:
        return ("No element in the list.")
    current_max = lst[0]
    for item in lst:
        if current_max < item:
            current_max = item
    return current_max

print(find_max(lst1))

#2 finding 2nd largest number in the list

lst2 = [1,1,1,1,1,1]

def scnd_lrgst(lst):
    if len(lst)<2:
        return "Provided list is not valid"
    first = lst[0]
    second = float('-inf')
    for item in lst:
        if item > first:
            second = first
            first = item 
        elif second < item and item != first:
            second = item
    if second == float('-inf'):
        return "All of the elements in the list is the same.So, No distinct 2nd largest nummber exist"
    return second
print(scnd_lrgst(lst2))

#4 count occurances of target elements

lst4 = [1,1,1,1,1,12,23,545]
def cnt_ocr(lst,target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count
print(cnt_ocr(lst4,1))