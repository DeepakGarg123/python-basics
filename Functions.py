"""Q1. Make a function that prints Welcome to Python Programming two times
def Welcome():
    print("Welcome to Python Programming")
Welcome()
Welcome()
"""

"""Q2. Create a function name add that performs addition of two numbers

def add(a, b):
    print(a+b)
add(10 , 20)
"""

"""Q3. Create a function name multiply that performs multiplication of two numbers

def multiply(a , b):
    print(a*b)
multiply(5 , 4)
"""

"""Q4. Create a function subtract that performs subtraction of two numbers.

def subtract(a , b):
    print(a-b)
subtract(9 , 5)
"""

"""Q5. function to find square

def square(a):
    print(a*a)
square(5)
"""

"""Q6. Check even or odd number

def even_odd(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
even_odd(7)
"""

"""Q7. Find largest of two numbers

def find_largest(a , b):
    if a>b:
        print("a is largest")
    else:
        print("b is largest")
find_largest(15 , 20)
"""

"""Q8. Calculate the average for three numbers

def average(a , b , c):
    avg = (a + b+ c)/3
    print(avg)
average(70 , 80 , 90)
"""

"""Q9. Function to check positive , negative or zero

def check(num):
    if num>0:
        print("Positive")
    elif num==0:
        print("Zero")
    else:
        print("Negative")
check(-5)
"""    

"""Q10. Function to count even numbers in a list

def even_numbers(num):
    count = 0
    for i in num:
        if i%2==0:
            count+=1
    print(count)
even_numbers([10 , 15 , 20 , 25 , 30 , 40])
"""

"""Q11. Create a function find largest number.

def find_largest(number):
    largest = number[0]
    for i in number:
        if i>largest:
            largest = i
    print(largest)
find_largest([10 , 15 , 20 , 25 , 630])
"""

"""Q12. Function to remove a list"""

def reverse_list(list):
    result = []
    for i in range(4 , -1 , -1):
        result.append(list[i])
    