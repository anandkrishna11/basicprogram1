'''author:Anand Krishna M A
date:25-10-2024
description:program to calculate the sum of digits of a number'''

number=int(input("Enter the number:"))
sum_digits=0
while number!=0:
    remainder=number%10
    sum_digits+=remainder
    number=number//10
print("sum of the digits of the given number is:",sum_digits)