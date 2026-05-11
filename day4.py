# reverse a string without using [::-1]
string = "Omprakash"
x = len(string)
revstring = ''
while x > 0:
    revstring += (string[x-1])
    x-=1
print(revstring)

# check char by char using two pointer , check for palindrome 


