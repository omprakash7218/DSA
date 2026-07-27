#ANAGRAMS - two words those who share same characters(alphabets) and means different. eg: tea ate , dear read,etc

def check_anagrams(a,b):
	if sorted(a) == sorted(b):
		print("ANAGRAMS")
	else:
		print("NOT ANAGRAMS")

check_anagrams("tea","ateb")

# write a programm that gives all the factor of a given number 

def factors(n):
	lst = []
	for i in range(1,int(n**0.5)+1):
		if n % i == 0:
			lst.append(i)
			# problem when we have a perfect square
			if i != n//i:
				lst.append(n//i)
		else:
			continue
		i+=1
	return lst
		
print(factors(25))

from math import sqrt

n = 25
result = []
for i in range(1,int(sqrt(n))+1):
	if n%i == 0:
		result.append(i)
		if n//i != i:
			result.append(n//i)
	else: 
		continue
	i+=1
result.sort()
print(result)


# store frequencies in dictionary from an array

array = [2,3,5,5]

dic = {}
for i in array:
	dic[i] = dic.get(i,0)+1            # .get is very important in hashing too.

print(dic)

# without using .get method

nums = [1,2,3,2,4,3,3]
frequency_map = {}
for i in range(len(nums)):
	if nums[i] in frequency_map:       # dictionary mein if statement tc O(N)
		frequency_map[nums[i]]  +=  1
	else:
		frequency_map[nums[i]] = 1
print(frequency_map)


# what is hashing 

# prestoring values inside a tuple or list or dict , to solve questions we say we are using hashing method