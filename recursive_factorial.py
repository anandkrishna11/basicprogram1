'''author:Anand Krishna M A
Description:Program to find the factorial of a number using Recursion.
Date:29-11-2024'''

def recursive_factorial(num):
    if num==1:
        return 1
    else:
        return num*recursive_factorial(num-1)
num1=int(input("Enter the number:"))
print(recursive_factorial(num1))