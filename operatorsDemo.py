'''author:Anand Krishna M A
date:18-10-2024
discription:Python program that demonstrates the usage of arithmetic, comparison, and logical operators. Perform a few operations and print the results.
output example:Sum: 15, Division: 2.0

Is a greater than b?: True

Are a and b equal?: False

Logical AND: True

Logical OR: True'''


number1=int(input("enter the number 1:"))
number2=int(input("enter the number 2:"))
print("sum:",number1+number2,',',"division:",number1/number2)

condition1=number1>number2
print("is number1 grater than number2?",condition1)

condition2=number1==number2
print("are number1 and number2 equal?",condition2)

print("Logical AND:",condition1 and condition2)
print("Logical OR:",condition1 or condition2)
