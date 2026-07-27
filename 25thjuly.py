# Basic_math_logic_buildup revision

# Extraction of digits from an integer

from ast import LShift


num = 123456213
n = num
lst = []
while n > 0:
    x = n%10 
    lst.append(x)
    n = n//10

lst.sort()

print(lst)


# count the number of digits 

num = 0
n = num 
count = 0
while n > 0:
    n =   n // 10
    count += 1 

print(count)

# using log method 

import math
n = -1223
if n == 0:
    print(0)
else:
    digits = math.floor(math.log10(abs(n)))+1
    print(digits)

# part 2 
from math import * 

n = 0
def find_number_of_digits(n):
    if n == 0:
        return 0
    else:
        return int(log10(abs(n))+1) 
print(find_number_of_digits(n))

# reverse a digit 

num = -12312

sign = -1 if num<0 else 1
n = abs(num)
rev = 0
while n>0:
    digit = n%10
    rev = rev * 10 + digit
    n = n//10
print(rev*sign)

# check if a  a palindrome 
nums = 121
def check_palindrom(nums):
    sign = 1 if nums > 0 else -1
    reverse = 0
    n = abs(nums)
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit 
        n = n//10
    reverse = reverse * sign
    if reverse == nums:
        return ("Palindrome!")
    else: 
        return ("Not a palindrome")        

print(check_palindrom(nums))
## if a number Armstrong number 

number = 153
def check_armstrong_or_not(number):
    number1 = number
    number2 = number 
    power = 0
    while number2 > 0:
        number2 =number2//10 
        power += 1
    probable_arm = 0    
    while number1 > 0:
        digit = number1 % 10
        probable_arm = probable_arm + digit **power
        number1 = number1 // 10 
    if probable_arm == number :
        return ("GG , You have found an Armstrong number.")
    else: 
        return ("Sorry! This is not an Armstrong nubmer ")
print(check_armstrong_or_not(11))