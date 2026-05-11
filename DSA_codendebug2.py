count = 0
def greet():
    global count
    if count == 4:
        return "nothing"
    print("omprakash chaudhary")
    count += 1
    greet()
greet()
# RECURSION HEAD AND TAIL TYPE
# print x a number n times 
# head recursion
def func(x,n):
    if n == 0:
        return
    print(x)
    func(x,n-1)
func(5,5)

# tail recursion
def funct(x,n):
    if n==0:
        return
    funct(x,n-1)
    print(x)
funct(1,5)

# print(1 to n) using recursion 

def ap(n,i =1):
    if i > n:
        return
    print(i)
    i += 1
    ap(n,i)
ap(80)
def apt(n,i = 1):
    if i > n:
        return 
    apt(n,i+1)
    print(i)

apt(5)
# but we have to print without using an extra variable i.e i 
def apw(n):
    if n == 0:
        return 
    print(n)
    apw(n-1)
apw(4)

def apwt(n):
    if n == 0:
        return 
    apwt(n-1)
    print(n)

apt(996)

# sum of 1st n natural number using recursion *parameterized & funtional recursion
#parameterized
def total(sum,i,n):
    if i > n:
        print(sum)
        return
    total(sum+i,i+1,n)
total(0,1,5)
#functional recursion
def sum(n:int):
    if n == 0:
        return n
    return n + sum(n-1)
print(sum(8))
# factorial using functional recursion 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
# using back tracking for both sum and factorial using functional Recursion 
def total (n):
    if n == 1:
        return 1
    
    return  (total(n-1)+n)
(total(5))
# 1 sec delayed view of recursion 
from operator import index
from subprocess import list2cmdline
import time
def total(n):
    if n == 1:
        print("Base case reached:", n)
        time.sleep(1)
        return 1
    print("Going DOWN:", n)
    time.sleep(1)
    result = total(n - 1)
    print("Coming UP:", n, "+", result)
    time.sleep(1)
    return result + n
print("Final Answer:", total(5))

# ? reversing an array using recursion 
# without using recursion

lst = [1,2,3,4,5,6,7,78]
def rev_lst(lst):
    lst2 = []
    n = len(lst)
    while n >= 1:
        lst2.append(lst[n-1])
        n -= 1
    return lst2
print(rev_lst(lst))

# using Recursion 

lst = [1,2,3,4,5,6,7,78]
def rev(l,r,lst):
    if l>=r:
        return lst
    # swap
    lst[l] , lst[r] = lst[r] , lst[l]
    return rev(l+1,r-1,lst)
print(rev(0,len(lst)-1,lst))

# using while loop :
lst= [1,2,3,4,5,6,7,8,9,10]
def revw(lst,l,r):
    while l<r:
        lst[l],lst[r]=lst[r],lst[l]
        l += 1
        r -= 1
    return lst
print(revw(lst,0,len(lst)-1))

# without using a function 

lst= [1,2,3,4,5,6,7,8,9,10]
l =0
r = len(lst)-1
while l<r:
    lst[l],lst[r]=lst[r],lst[l]
    l += 1
    r -= 1
print(lst)
# Check if a string is palindrome or not using recursion
s = "aba"
if s == s[::-1]:
    print("palindrome")
else: 
    print("Not a palindrome")

# using loop and function 
s2 = "amaamaamaama"
def pal(string,l,r):
    while l<r:
        if string[l] == string[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

print(pal(s2,0,len(s2)-1))

# using recursion 
s3 = 'ama'
def palr(string,l,r):
    if l >= r:
        return True
    elif string[l]!=string[r]:
        return False
    return palr(string,l+1,r-1)

print(palr(s3,0,len(s3)-1))

#chatgpt version
def palr(string, l, r):
    print(f"Checking: {string[l]} vs {string[r]}")

    if l >= r:
        print("Reached middle → True")
        return True

    if string[l] != string[r]:
        print("Mismatch → False")
        return False

    return palr("string", l+1, r-1)
s4  = "ashdlf"
print(palr(s4,0,len(s4)-1))
# fibonacci series using recursion
# loop
i = 0
j = 1
print(i)
print(j)
while j <= 100:
    fib = i + j
    print(fib)
    i = j
    j = fib
print(fib) 

# recursion
# fibnocci number by index
class Solution:
    def fib(self, n: int):
        if (n==1 or n==0):
            return n
        elif n < 0:
            return "Please enter a number greater than or equal to "
        return self.fib(n-1)+self.fib(n-2)
    index = int(input("Please enter the index of your desired fibonacci number: "))
fib_index = Solution()
print(fib_index.fib(index))

# ! Selection sort 
arr = [4, 1, 3, 9, 7,0]


n = len(arr)
for i in range(0,n-1):
    min_index = i
    for j in range(i + 1,n):
        if arr[j]<arr[min_index]:
            min_index = j
    arr[min_index],arr[i]=arr[i],arr[min_index]        
print(arr)
# selection sort for descending order 

arr = [9,4,2,5,4,32,4,97,55,444]
n = len(arr)
for i in range(0,n-1):
    max_index = i 
    for j in range (i+1,n):
        if arr[j]>arr[max_index]:
            max_index = j
    arr[max_index],arr[i]=arr[i],arr[max_index]
print(arr)

# bubble sort 
