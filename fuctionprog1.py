'''Author:Anand Krishna M A
Description:Write a Python function to find the maximum of three numbers
Date:30-11-24'''

def max_num(x):
    print(f'max number={max(x)}')
num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
num3=int(input("enter the number3:"))
lst=[num1,num2,num3]
max_num(lst)