state = "Tamill Nadu"
if state.startswith("Tamil"):
    print("Chennai")
elif state.endswith("Nadu"):
    print("Banglore")
else:
    print("Patna")


# Introduction to  Hashing
n = [1, 2, 3, 4, 5, 6, 1, 1, 2, 4, 5, 6, 8]
m = [1, 12, 23, 2, 3, 4, 5, 6, 7, 8, 89, 9, -821]
freq_map = {}
for num in m:
    for x in n:
        if x == num:
            freq_map[num] = freq_map.get(num, 0) + 1
print(freq_map)

hash_list = [0] * 11
for i in n:
    hash_list[i] += 1
print(hash_list)
freq_maped = {}
for j in m:
    if j < len(hash_list) and j > 0:
        freq_maped[j] = freq_maped.get(j, 0) + hash_list[j]
print(freq_maped)

# using predifined dictionary (hashed dict)

hash_dict = {}
for num in n:
    hash_dict[num] = hash_dict.get(num, 0) + 1
final_dictionary = {}
for num in m:
    if num in hash_dict:
        final_dictionary[num] = hash_dict[num]
print(final_dictionary)
print("-------------------------------------")
p = "mynameisanthunigonjalwis"
q = ["a", "b", "c", "s", "d"]

hashed_dict = {}

for char in p:
    hashed_dict[char] = hashed_dict.get(char, 0) + 1
final_dict = {}
for char in q:
    if char in hashed_dict:
        final_dict[char] = hashed_dict[char]
print(final_dict)


# making this using ascii value of a - z

print(ord("a"))

s = "killsololevelingcharacterasap"
q = ["a", "b", "c", "s", "d"]

hashed_array = [0] * 26
for char in s:
    postion = ord(char) - 97
    hashed_array[postion] += 1

print(hashed_array)
dict_output = {}
for char in q:
    postion = ord(char) - 97
    if hashed_array[postion] > 0:
        dict_output[char] = hashed_array[postion]
print(dict_output)


# recursion


def greet():
    print("Hello everyone!")


greet()

# What if we want to greet 7 times in a row


def greet(num):
    if num == 0:
        return "Done"
    greet(num - 1)
    print("HELLO EVERYONE!")


(greet(7))

# print 1 - 5 using recursion


def fuc(i, n):
    if i > n:
        return
    print(i)
    fuc(i + 1, n)


fuc(2, 5)

# print 1 - 5 using tail recursion


def func(n):
    if n == 0:
        return
    func(n - 1)
    print(n)


func(6)
