# reverse a list without using reverse() attribute. 

lst = [1,2,3,4,5,6,7,8,9,10]
name = "Omprakash Chuudhary"
print(name[::-1])
# method 1 
print(lst[::-1])

# method 2 using while loop
lst2= []
index = len(lst)-1
while index >= 0:
    lst2.append(lst[index])
    index -= 1
print(lst2)
# method 3 using function recursion
def reverse_lst(lst,start,end):
    if start>=end//2:
        return
    lst[start],lst[end]=lst[end],lst[start]
    return reverse_lst(lst,start+1,end-1)
lst = [1,2,3,4,5,6,7,8,9,10]
end = len(lst)-1
(reverse_lst(lst,0,end))
print(lst)
# method 4 using swapping 
lst = [1,2,3,4,5,6,7,8,9,10]
n = len(lst)
for i in range(0,n//2):
    lst[i],lst[n-1-i] = lst[n-1-i],lst[i]

print(lst)