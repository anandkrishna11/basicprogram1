'''author:Anand Krishna M A
Description:Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
Date:30-11-2024'''

def factorial(x):
    fac=1
    for i in range(1,x+1):
        fac=fac*i
    return fac

num=int(input("Enter a positive number to find factorial:"))
print(factorial(num))