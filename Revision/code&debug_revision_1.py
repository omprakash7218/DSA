# Extraction digits from an integer.
# ? integer means +ve integer if negative just multiply num * -1 or abs(num)
from re import S


print(abs(-42))
def extract_digits(x):
    lst = []
    while x > 0:
        d = x%10 
        lst.append(d)
        x = x//10        
    return lst
print(extract_digits(124556))


# reverse a number 
def number_reverse(x):
    rx = 0
    while x > 0:
        rem = x%10
        rx = rx*10 + rem
        x = x//10
    return (rx)
print(number_reverse(1234))


#Check palindrome 
def check_palindrome(x):
    rx = 0
    while x > 0:
        rem = x %10
        rx = rx*10+rem
        x = x//2
    if x == rx:
        return("Palindrome")
    else:
        return("Not a palindrome")
print(check_palindrome(1210))


# check for armstrong number 
def armstng_check(x):
    ax = (x)
    pwr = len(str(ax))
    armstrng = 0
    while x > 0:
        rem = x %10
        armstrng = armstrng + rem**pwr
        x = x//10
    if armstrng ==(ax) :
        return ("Armstrong number")
    else:
        return ("Not a Armstrong number")
print(armstng_check(10))

#counting the no. of digits in an integer
def count_digit(x):
    count = 0
    while x >0:
        count += 1
        x = x//10
    return count
print(count_digit(-1574))


#store frequency in dictionary
# my approach was wrong , i did look into the provious code of mine which was also not acceptable.
nums = [5,6,7,7,1,9,111,1,1,5,1,1,1,5,5,5,5,7,7,7,12,1,2,2,2,3,3,3,47,4,4,4,5,5,56,6,6,6,6,6,7,7,7,7,1,0,10,1,0,12]
n = len(nums)
freq = {}
for l in range(0,n-1):
    count = 1
    for r in range(l+1,n):
        if nums[l] == nums[r]:
            count += 1 
    if nums[l] in freq:
        continue
    else:
        freq[nums[l]]=count    # key should alwaays be unique
print(freq)

# correct approach 
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i]=1
print(freq)

# Hashing in python # !
# ? Prestoring values into some data structure like List/Dictionary/set and then fetching it 
nums = [5,6,7,7,1,9,111,1,1,5,1,1,1,5,5,5,5,7,7,7,12,1,2,2,2,3,3,3,47,4,4,4,5,5,56,6,6,6,6,6,7,7,7,7,1,0,10,1,0,12]

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
# Q1.n = [5,3,2,2,1,5,5,7,5,10]  &  m = [10,111,1,9,5,67,2] 
# constraints 1. 1<n[i]<=10 2. n&m can have 10**8 elements
# QQ. how many times the values inside m has occurred inside of n
n = [5,3,2,2,1,5,5,7,5,10]   
m = [10,111,1,9,5,67,2] 
repeat = {
}
for i in m: 
    count = 0
    for j in n:
        if i == j:
            count += 1
    if i in repeat:
        continue
    elif i > 10:
        continue
    else:
        repeat[i]=count
print(repeat) 
# Hash map way 
n = [5,3,2,2,1,5,5,7,5,10]   
m = [10,111,1,9,5,67,2] 
hash_map = {}
for num in n: 
    hash_map[num]=hash_map.get(num,0)+1

for num in m:
    if num in hash_map:
        print(f"{num}:{hash_map[num]}")

# s = "azyxyyzaaaa" , q = ['d','a','y','x']  constraints 1. 'a'<s[i]<='z'
s = "azyxyyzaaaa" 
q = ['d','a','y','x']
hash_map = {}

for string in s:
    hash_map[string]=hash_map.get(string,0)+1
print(hash_map)
for string in q: 
    if string in hash_map:
        print(f'{string}:{hash_map[string]}')

# check if a string is palindrome or not catch!- use recursion

s = 'naman'
n = len(s)
is_palindrome = True
for l in range(0,int(n/2+1)):
        if s[l]!=s[n-1-l]:
            is_palindrome = False
if is_palindrome == False:
    print("Not a palindrome")
else:
    print("Palindrome")

def check(s,l,r):
    if s[l] != s[r]:
        return "Not a Palindrome"
    elif l >= r:
        return "Palindrome"
    return check(s,l+1,r-1)
s = 'naman'
print(check(s,0,len(s)-1))

# reverse an array using Recursion

ar = [1,2,3,4,5,6,7,8,9,10]
def r_ar(ar,l,r):
    if l>=r:
        return ar
    ar[l],ar[r] = ar[r],ar[l]
    return r_ar(ar,l+1,r-1)
print(r_ar(ar,0,len(ar)-1))

# find the fibinacci number using array
# fn = fn-1+fn-2
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(11))