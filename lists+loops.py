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

"""Q8. Seperate even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []
for i in numbers:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)
"""

"""Q9. Search an element
numbers = [10, 25, 30, 45, 50]

numbers = [10, 25, 30, 45, 50]
Found = False
for i in numbers:
    if i==30:
        Found=True
if Found==True:
    print("found")
else:
    print("Not found")
"""    
"""Q10. Remove duplicates
numbers = [10, 20, 10, 30, 20, 40, 30]

numbers = [10, 20, 10, 30, 20, 40, 30]
result = []
for i in numbers:
    if i not in result:
        result.append(i)
print(result)
"""

"""Q11. Calculate Average
numbers = [70, 80, 90, 60, 100]

numbers = [70, 80, 90, 60, 100]
total = 0
for i in numbers:
    total = total+i
    average = total/len(numbers)
print(average)
"""

"""Q12.Find the second largest number
numbers = [10, 50, 30, 90, 70, 80]

numbers = [10, 50, 30, 90, 70, 80]
largest = numbers[0]
second_largest = numbers[0]
for i in numbers:
    if i>largest:
        second_largest = largest
        largest = i
    elif i>second_largest:
        second_largest =i
print(second_largest)
"""

    
    