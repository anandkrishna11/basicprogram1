"""author:Anand Krishna M A
date:25-10-2024
discription:Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
sample output:The largest number is: 78"""

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if num2<num1>num3:
    print("The largest number is:",num1)

elif num1<num2>num3:
    print("The largest number is:",num2)

else:
    print("The largest lumber is:",num3)