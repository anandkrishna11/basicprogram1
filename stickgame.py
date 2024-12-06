stick=16
name1=input("Enter name of player1:")
name2=input("Enter name of player2:")
def stick_pick(x,y):
    if x>3:
        print("you can only pick upto 3 sticks!")
    else:
        if y>=3:
            print(f"you pick {x} stick and remaining {y-x} sticks")
            a=y-x
        elif y==2:
            if x>y:
                print("you can only take upto 2 sticks")
                x=int(input("re enter the no of sticks you want to pick:"))
                print(f"you pick {x} stick and remaining {y - x} sticks")
                a=y-x
            else:
                print(f"you pick {x} stick and remaining {y - x} sticks")
                a = y - x
        elif y==1:
            print("last stick you picked")
            a=0
    return a
while True:
    if stick>0:
        print(name1," chance")
        a1=int(input("enter the no. of sticks you want to pick"))
        res=stick_pick(a1,stick)
        stick=res
        if stick==0:
            print(name2,"wins")
        print(name2," chance")
        a2=int(input("Enter the no. of sticks you want to pick"))
        res2=stick_pick(a2,stick)
        stick=res2
        if stick==0:
            print(name1,"wins")
    elif stick==0:
        print("Game Over")
        break



