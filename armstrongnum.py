'''Author:Anand Krishna M A
Date:25-10-2024
description:program to check weather the number is armstrong or not'''

number=int(input("Enter the number"))
armstrong=0
number2=number
while number2!=0:
    num=(number2%10)**3
    armstrong+=num
    number2=number2//10
if number==armstrong:
    print(number,"is an armstrong number!")



