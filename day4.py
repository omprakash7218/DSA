# # reverse a string without using [::-1]
# string = "Omprakash"
# x = len(string)
# revstring = ''
# while x > 0:
#     revstring += (string[x-1])
#     x-=1
# print(revstring)

# # check char by char using two pointer , check for palindrome 

ar = [1,2,3,4,1,5,2,1,3]
target = 3
seen = set()

for num in ar:
    compliment = target - num

    if compliment in seen:
        print(compliment, num)

    else:
        seen.add(num)
