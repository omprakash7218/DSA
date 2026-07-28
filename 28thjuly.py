# Parameterized and functional recursion

# sum of first n natural numbers
# functional recursion has 2 parts -- 1. base case , f(n) = 1 if n ==1 in this case 2. recursive case f(n-1)


# parameterized
def func(n, i=1, sum=0):
    if i > n:
        print(sum)
        return
    func(n, i + 1, sum + i)


(func(10))

# functional recursion


def func(n):
    if n == 1:
        return 1
    return n + func(n - 1)


print(func(4))


# find nth fibonacci no.abs
# base case fib(1) == 1 or fib(0) == 0
# recursive case fib(2) = fib(1)+fib(0)  fib(n)= fi(n-1)+fib(n-2)


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(8))


# find factorial of a number
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)


print(fact(3))

# reverse an array
# x = [1,2,4,"sdkfj","sdlkj",12]
# left = 0
# right = len(x)-1
# while left<right:
#     x[left],x[right] = x[right],x[left]
#     left +=1
#     right -=1
# print(x)
# using a recursion


def reverse_array(x, left=0, right=None):
    if right is None:
        right = len(x) - 1
    if left >= right:
        return x
    x[left], x[right] = x[right], x[left]
    return reverse_array(x, left + 1, right - 1)


z = [2, 4, 5, 6, 6, 7, 8, 9, 123]
print(reverse_array(z))
