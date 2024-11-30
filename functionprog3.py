'''author:Anand Krishna M A
Description:Write a Python function to sum all the numbers in a list.
Date:30-11-2024'''

def mul_lst(x):
    product=1
    for i in x:
        product=product*i
    return product
lst=eval(input("Enter the list of numbers:"))
print(mul_lst(lst))