'''Author:Anand Krishna M A
Description:Program to construct patterns of stars(*) using a nested for loop
Date: 22-11-2024'''

num1=int(input("Enter the number of rows :"))
print("1.Increasing Triangle 2.Decreasing Triangle 3.Hill pattern 4.Reverse Hill pattern")
opt=int(input("enter option:"))
if opt == 1:
    for i in range(1,num1+1):
        for j in range(i):
            print("*",end='')
        print()
if opt == 2:
    for i in range(num1,0,-1):
        for j in range(i):
            print("*",end='')
        print()
if opt == 3:
    for i in range(1,num1+1):
      for j in range(num1-i):
          print(" ",end=" ")
      for k in range(2*i-1):
          print('*',end=" ")

      print('')
if opt == 4:
    for i in range(num1,0,-1):
        for j in range(num1 - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print('*', end=" ")
        print('')




