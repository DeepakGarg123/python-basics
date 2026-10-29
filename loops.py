"""Print numbers from 1 to 10
for i in range(1 , 11):
    print(i)
"""    

"""Sum of numbers from 1 to 10
total = 0
for i in range(1 , 11):
    total = total + i
print(total)
"""

"""Multiplication table

number  = int(input("Enter the number:"))
for i in range(1 , 11):
    total = number*i
    print(total)
"""

"""check even numbers from 1 to 20

count = 0
for i in range(1 , 21):
    if i%2==0:
        count = count+1
print(count)
"""

"""FizzBuzz Problem 
Task: Print numbers from 1 to 15, following these rules:
- If a number is divisible by both 3 and 5, print FizzBuzz.
- If divisible by 3 only, print Fizz.
- If divisible by 5 only, print Buzz.
- Otherwise, print the number itself.

for i in range(1 , 16):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
"""        

"""Sum of even numbers from 1 to 20

count = 0
for i in range(1 , 21):
    if i%2==0:
        count = count + i
print(count)
"""

"""Difficulty: Intermediate

Problem: Write a Python program that prints all numbers from 1 to 50 that are divisible by 3 but NOT divisible by 5. At the end, print how many such numbers were found.

count = 0
for i in range(1 , 51):
    if i%3==0 and i%5!=0:
        print(i)
        count = count+1
print(count)
"""
"""factorial of a number

number = 4
factorial = 1
for i in range(1 , number + 1):
    factorial = factorial*i
print(factorial)
"""

"""Calculate the sum of factorial from 1 to 4
total = 0
for number in range(1 , 5):
    factorial = 1
    for i in range(1 , number +1):
        factorial = factorial*i
    total = total+factorial
print(total)
"""

""" Print a number pattern
for i in range(1  , 6):
    for j in range(1 , i+1):
        print(j , end = "")
    print()
""" 
 
""" Print a number pattern 
 1
 21
 321
 4321
 54321


for i in range(1 , 6):
    for j in range(i , 0 , -1):
        print(j , end="")
    print()
"""




