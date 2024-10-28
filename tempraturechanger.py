'''Author:Anand krishna M A
date:28-10-2024
description:Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:
   1. Convert Celsius to Fahrenheit
   2. Convert Fahrenheit to Celsius
   3.Exit the program'''

while True:
    print("1.Convert Celsius to Fahrenheit")
    print("2.Convert Fahrenheit to Celsius")
    print("Exit the program")
    ch=int(input("Enter your choice"))
    if ch==1:
        cel=float(input("Enter the temperature in celsius"))
        fah=(cel*9/5)+32
        print(f"{cel} celsius in fahrenheit is:{fah}")
    elif ch==2:
        fah=float(input("Enter the temperature in fahrenheit"))
        cel=(fah-32)*5/9
        print(f"{fah}fahrenheit in celsius is:{cel}")
    elif ch==3:
        break
    else:
        print("INVALID CHOICE! SELECT(1,2,3)")
