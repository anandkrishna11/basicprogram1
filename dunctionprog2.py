'''author:Anand Krishna M A
Description:Write a Python function to sum all the numbers in a list.
Date:30-11-2024'''

def sum_lst(x):
    sum=0
    for i in x:
        sum+=i
    return sum
lst=eval(input("Enter the list of numbers:"))
print(sum_lst(lst))