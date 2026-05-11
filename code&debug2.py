# Print factors of the given numbers
num = 15 
# brute force method
def factors(num):
    lst = []
    for i in range(1,num+1):
        if num%i == 0:
            lst.append(i)
    return lst
print(factors(num))

# better method 
def factorsb(num):
    lst = []
    for i in range(1,num//2):
        if num % i == 0:
            lst.append(i)
    lst.append(num)
    return lst
print(factorsb(num))

# optimal method 
def factorso(num):
    lst = []
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            div = num//i
            lst.append(i)
            if div != i:
                lst.append(div)
        lst.sort()
    return lst
print(factorso(35))