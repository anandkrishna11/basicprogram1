'''author:Anand Krishna M A
Description:Write a Python function to check whether a number falls within a given range..
Date:30-11-2024'''

def up_low_case(x):
    up_count=0
    low_count=0
    for i in x:
        if i.isupper():
            up_count+=1
        elif i.islower():
            low_count+=1
        else:
            pass
    print("upper case count=",up_count)
    print("lower case count=",low_count)
str1=input("Enter the string:")
up_low_case(str1)

