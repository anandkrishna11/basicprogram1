def right_triangle(x,y,z):
    if (x**2)+(y**2)==z**2:
        print("The given triangle is a right triangle")
    elif (y**2)+(z**2)==x**2:
        print("The given triangle is a right triangle")
    elif (z**2)+(x**2)==y**2:
        print("The given triangle is a right triangle")
    else:
        print("The given triangle is not a right triangle.")
while True:
    side1=int(input("Enter the length of first side:"))
    side2=int(input("Enter the length of second side"))
    side3=int(input("Enter the length of third side:"))
    right_triangle(side1,side2,side3)
    ask=input("Do you want to try another triangle(Y/N):")
    if ask in 'Nn':
        break

