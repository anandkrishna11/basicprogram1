''''author:Anand Krishna M A
date:25-10-2024
description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c5=f−329'''

temperature=int(input("Enter the temperature:"))
ask=input("Is this in (C)celsius or (F)fahrenheit?")
if ask=='c'or'C':
    result=((9/5)*temperature)+32
    print(temperature,"celsius is",result,"fahrenheit")
elif ask=='F'or'f':
    result=(5/9)*(temperature-32)
    print(temperature, "fahrenheit is", result, "celsius")
else:
    print("print a valid option(c/f)")
