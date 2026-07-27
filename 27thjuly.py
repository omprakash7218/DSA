state =  "Tamill Nadu"
if state.startswith("Tamil"):
    print("Chennai")
elif state.endswith("Nadu"):
    print("Banglore")
else:
    print("Patna")


# Introduction to  Hashing 
n = [1,2,3,4,5,6,1,1,2,4,5,6,8]
m = [1,12,23,2,3,4,5,6,7,8,89,9,-821]
freq_map = {}
for num in m: 
    for x in n : 
        if x == num : 
            freq_map[num] = freq_map.get(num,0)+1
print(freq_map)

hash_list = [0]*11
for i in n:
    hash_list[i] += 1
print(hash_list)
freq_maped = {}
for j in m:
    if j < len(hash_list) and j > 0:
        freq_maped[j] = freq_maped.get(j,0)+hash_list[j]
print(freq_maped)

# using predifined dictionary (hashed dict)

hash_dict = {}
for num in n:
    hash_dict[num] = hash_dict.get(num,0) + 1
for num in m: 
    if num in hash_dict:
        print(f"{num} : {hash_dict[num]}")

print("-------------------------------------")
p = "mynameisanthunigonjalwis"
q = ["a","b","c","s","d"]

hashed_dict ={}

for char in p :
    hashed_dict[char] = hashed_dict.get(char,0)+1

for  char in q : 
    if char in hashed_dict:
        print(f"{char} : {hashed_dict[char]}")