"""Print lists
fruits = ["Apple" , "Banana" , "Mango" , "Guava" , "Cherry"]
print(fruits)
"""

"""Accessing an elemnt
numbers = [10, 20, 30, 40, 50]
print(numbers[2])
"""

"""Append
numbers= [10 , 20 , 30]
numbers.append(40)
print(numbers)
"""

"""Remove
numbers = [5, 10, 15, 20, 25]
numbers.remove(15)
print(numbers)
"""

"""Insert
numbers = [10, 20, 40, 50]
numbers.insert(2,30)
print(numbers)
"""

"""POP
fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.pop()
print(fruits)
"""

"""List Length
numbers = [12, 24, 36, 48, 60, 72]
print(len(numbers))
"""

"""Loop+ list
numbers = [10, 20, 30, 40, 50]
for i in numbers:
    print(i)
"""

"""Q1. Sum of list

numbers = [10, 20, 30, 40, 50]
total = 0
for i in numbers:
    total = total+i
print(total)
"""

"""Q2. Count even numbers
numbers = [12, 7, 18, 5, 20, 9, 14]
count = 0
for i in numbers:
    if i%2==0:
        count+=1
print(count)
"""

"""Q3. Find the largest number

numbers = [23, 67, 12, 89, 45, 34]
largest = numbers[0]
for i in numbers:
    if i>largest:
        largest = i
print(largest)
"""

"""Q4. Problem - numbers = [1 , 2 , 3 , 4 , 5]
we have to double the list using for loops
Output : numbers = [2 , 4 , 6 , 8 , 10]

numbers = [1 , 2 , 3 , 4 , 5]
result = []
for i in numbers:
    result.append(i*2)
print(result)
"""

"""Q5. Reverse a list
numbers = [10 , 20 , 30 , 40 , 50]

numbers = [10 , 20 , 30 , 40 , 50]
result = []
for i in range(4 , -1 , -1):
    result.append(numbers[i])
print(result)
"""

"""Q6. Count Positive numbers
numbers = [10 , -5 , 20 , -8 , 0 , 15 , -2]

numbers = [10 , -5 , 20 , -8 , 0 , 15 , -2]
count = 0
for i in numbers:
    if i>0:
        count+=1
print(count)
"""

"""Q7. Find Smallest number
numbers = [45, 12, 78, 5, 34, 89]

numbers = [45, 12, 78, 5, 34, 89]
smallest = numbers[0]
for i in numbers:
    if i<smallest:
        smallest = i
print(smallest)
"""


