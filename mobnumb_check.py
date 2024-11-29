'''author:Anand Krishna M A
Description:Program to check whether the given number is a valid mobile number or not using functions
Date:29-11-24'''

def valid_mob(x):
    a= str(x)
    if len(a)==10 and a[0] in '789':
        print(f"{x} is a valid mobile number")
    else:
        print("invalid mobile number")
mob=int(input("Enter the mobile number"))
valid_mob(mob)