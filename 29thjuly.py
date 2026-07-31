# Learn Dict and set fundamentals , frequency counting patterns , two sum family of problems 

# given a string , return the first character that appear exactly once
def index_non_repeating(word:str):
    hash_map = {}
    for ch in word :
        hash_map[ch] = hash_map.get(ch,0)+1
    for i in range(len(word)):
        if hash_map[word[i]] == 1:
            return i
    return -1
print(index_non_repeating("leetcode"))
print(index_non_repeating("loveleetcode"))
print(index_non_repeating("aabb"))

# find the most frequent element
def most_freq(arr):
    freq_map = {}
    max = 0
    answer = None
    for item in arr:
        freq_map[item] = freq_map.get(item,0)+1
    for key,value in freq_map.items():
        if value > max:
            max = value
            answer = key

    return answer 


print(most_freq([1,2,3,4,1,1,1,1,1,2,2,2,2,4]))


# check two strings are anagrams 

a = "tea"
b = "eatd"


def check_anagram(a,b):
    if len(a) != len(b):
        return False
    dic_a = {}
    dic_b = {}
    for ch in a:
        dic_a[ch] = dic_a.get(ch,0) + 1
    for ch in b:
        dic_b[ch] = dic_b.get(ch,0) + 1
    return dic_a == dic_b
print(check_anagram(a,b))

# 1. Two Sum — Return values, not indices, unsorted array, avoid duplicate pairs
arf = [2,34,5,32,5,5,5,5,52,1,1,34,5,6,9]
target = 7
# brute force method 
# for a in range(len(arf)-1):
#     for b in range(a+1,len(arf)):
#         if arf[a] + arf[b] == target:
#             print(arf[a],arf[b])
#         else: 
#             continue


# optimal way using set 
ar = [1,2,3,4,1,5,2,1,3]
target = 3
seen = set()

for num in ar:
    compliment = target - num
    if compliment in seen:
        print(compliment,num)

    else:
        seen.add(num)