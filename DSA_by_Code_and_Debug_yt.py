lst = [1,2,3,4,7,-2,4,2,54654,654,5,5,654,5,8,5,8,5,825,8,5,85,5]
# ? we are going to find maximum and minimum without using any method of list data type.
# 1st attempt
smallest = lst[0]
largest = lst[0]
for i in lst:
    if i < smallest:
        smallest = i
    elif len(lst)==0:
        print("No items in the list")        
    else:
        continue
print("Smallest number in the list: ",smallest)

for i in lst:
    if i > largest:
        largest = i
    elif len(lst)==0:
        print("No item in the list")
    else:
        continue
print("Largest number in the list: ",largest)
# 2nd attempt
smallest = lst[0]
largest = lst[0]
for i in lst:
    if len(lst)==0:
        print("No items in the list")
    elif i > largest:
        largest = i
    elif i < smallest:
        smallest = i        
    else:
        continue
print("Smallest number in the list: ",smallest)
print("Largest number in the list: ",largest)

for i in lst:
    if i > largest:
        largest = i
    elif len(lst)==0:
        print("No item in the list")
    else:
        continue


def largest_smallest(lst):
    smallest = lst[0]
    largest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
        elif len(lst)==0:
            print("No items in the list")        
        elif i > largest:
            largest = i
        else:
            continue
    print("Smallest number in the list: ",smallest)
    print("Largest number in the list: ",largest)

largest_smallest(lst)
# ? calculate the number of elements in the list
# chat gpt version of the question 

def find_min_max(numbers):
    # Edge case: Return None if the list is empty to prevent errors
    if not numbers:
        return None, None
    
    # 1. Assume the first number is both the smallest and the largest
    min_val = numbers[0]
    max_val = numbers[0]
    
    # 2. Ldeoop through every number in the list
    for num in numbers:
        # 3. Check if the current number is smaller than our record
        if num < min_val:
            min_val = num
            
        # 4. Check if the current number is larger than our record
        if num > max_val:
            max_val = num
            
    return min_val, max_val

# --- Example Usage ---
my_list = [34, 12, 5, 78, 2, 99, 45]
smallest, largest = find_min_max(my_list)

print("Minimum number is:", smallest)
print("Maximum number is:", largest)

def len(lst):
    count = 0 
    for items in lst:
        count += 1
    print(count)
len(lst)

# ? sum of all elements of a list
def sum(lst):
    sum = 0
    for items in lst:
        sum += items
    print(sum)
sum(lst)

# count even and odd numbers in an array
def even_odd(lst):
    count_even = 0
    count_odd = 0
    for items in lst:
        if items%2==0:
            count_even += 1
        else:
            count_odd += 1
    print("Even numbers in the list: ",count_even)
    print("Odd numbers in the list: ",count_odd)
even_odd(lst)