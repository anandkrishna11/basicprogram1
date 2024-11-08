num1=int(input("How many numbers do you want to enter?"))
num=int(input("Enter a number"))
greatest=num
smallest=num
for i in range(1,num1+1):
    n1 = int(input("enter number:"))
    if greatest < num:
        greatest = num
    elif smallest > num:
        smallest = num
print(f"the greatest number is:{greatest}")
print(f"the smallest number is:{smallest}")

