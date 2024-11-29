def recursive_addition(x,y):
    if y==0:
        return x
    else:
        return recursive_addition(x+1,y-1)
num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2:"))
print(f"sum={recursive_addition(num1,num2)}")