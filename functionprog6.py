'''author:Anand Krishna M A
Description:Write a Python function to check whether a number falls within a given range..
Date:30-11-2024'''

def range_check(x,y,z):
    if x in range(y,z+1):
        print(f"{x} is in the given range")
    else:
        print(f"{x} is not in the given range")
r1=int(input("Enter the beginning of range:"))
r2=int(input("Enter the ending of range:"))
while True:
    num=int(input("Enter the number to check:"))
    range_check(num,r1,r2)
    a1=input("Do you want to try another number(Y/N):")
    if a1 in 'Nn':
        break