'''Author:Anand Krishna M A
Date:18-10-2024
Discription:Python program that uses functions from the math module to perform the following operations on a number provided by the user
output example:Enter a number: 5

Square root of 5: 2.23606797749979

Factorial of 5: 120

5 raised to power 2: 25.0'''
import math
number=int(input("Enter a number:"))
print("square of root",number,':',math.sqrt(number))
print("Factorial of",number,':',math.factorial(number))
print(number,"raised to power 2:",math.pow(number,2))

