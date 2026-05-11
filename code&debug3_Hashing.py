# Frequency map/ dictionary
# store frequency in dictionary
nums = [1,1,54,9,4,4,4,4,4,4,4,5656,56,5,5,5,5,58,87657,54,23421,654,68434,21,68,54,34,654,654,654,654,46,54,46,4,1,1,1,1,2,2,2,2,2,3,3,3,3,5,5,5,5,5,45,4,4,4,4,4,66,9,6,6,6]
freq_map = {}
for i in nums:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i]=1   
print(freq_map)
#-----------------------------------------------------
hash_map = dict()
n = len(nums)
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)

# ! Hashing in python but as a concept it will work in all of the programming language
# ? Prestoring values into some datastructure like List/Dictionary/sets and the fetching it.

# Q1.n = [5,3,2,2,1,5,5,7,5,10]  &  m = [10,111,1,9,5,67,2,10] ] 
# constraints 1. 1<n[i]<=10 2. n&m can have 10**8 elements
# QQ. how many times the values inside m has occurred inside of n

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2,10]
hash_list = [0]*11
for num in n:
    hash_list[num]+=1
for item in m:
    if item >10 or item <1:
        continue
    else:
        print(item,":",hash_list[item])
    
# 2nd method dict
# constraints 1. 1<n[i]<=10 2. n&m can have 10**8 elements
# QQ. how many times the values inside m has occurred inside of n
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2,10]
hash_map = {}
for item in n:
    hash_map[item]  = hash_map.get(item,0) + 1
for key in m:
    if key >10 or key<1:
        continue

    print(f"{key}: {hash_map.get(key,0)}")


# s = "azyxyyzaaaa" , q = ['d','a','y','x']  constraints 1. 'a'<s[i]<='z'
# ? ASCII code of all the letters and symbol
# ? prerequisite
# ? 1. print(ord('a'))   2. print(chr(97))
s = "azyxyyzaaaa" 
q = ['d','a','y','x']

hash_list = [0]*27
for ch in s:
    index = ord(ch)-96
    hash_list[index] += 1
for ch in q:
    index = ord(ch)-96
    print(f"{ch}: {hash_list[index]}")
