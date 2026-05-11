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
# method 3 usinf function recursion

