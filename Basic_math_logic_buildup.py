
# ! Extraction of digit from an integer.
# n = int(input("Enter your number here: "))
n = 7010
while n > 0:
    remain = n%10
    print(remain)
    n = n//10
print(type(n))
nst = str(n)
print(len(nst))
print(len('710'))
# ? count the number of digits in an integer 
# n = int(input("Your number here: "))
n2 = 8789
count = 0
while n2 > 0 :
    count += 1
    n2 = n2//10
print(count)
# palindrome 
n3 = 2345
palindrome_or_not = 0

while n3 > 0:
    add = n3%10
    palindrome_or_not = palindrome_or_not*10+add
    n3 == n3//10
if palindrome_or_not == n3: 
    print("Hurray! we have a palindrome.")
else:
    print("So sorry! we don't have a palindrome.")


# Armstrong number 
# n = int(input("Enter your number: "))

num = 0
def armstng_check(num):
    actual_num = (num) 
    power = len(str(num))
    total = 0
    while num >0:
        remain = num % 10 
        total += remain**power
        num = num//10
    if actual_num == total:
        return "Congratulations! you have got an Armstrong Number."
    return "Sorry! the number given by is not an Armstrong Number."
print(armstng_check(num))



