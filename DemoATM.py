''''Author:Anand Krishna M A
Date:2-10-2024
Description:program that simulates a simple bank ATM system. The user has an initial balance of $1000. The ATM should display a menu with options to:
   1. Check Balance
   2. Deposit Money
   3.Withdraw Money
   4.Exit'''

balance_amount=1000
while True:
    print("1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"the current balance ${balance_amount}")
    elif choice==2:
        deposit_amount=float(input("Enter the amount to deposit:"))
        balance_amount=balance_amount+deposit_amount
        print(f"The deposited amount ${deposit_amount} and The current balance is{balance_amount}")
    elif choice==3:
            withdraw_amount = float(input("Enter the amount to withdraw:"))
            if withdraw_amount>balance_amount:
                print("Insufficient Balance")
            else:
                balance_amount = balance_amount - withdraw_amount
                print(f"The withdrawn amount ${withdraw_amount} and the current balace is{balance_amount}")
    elif choice==4:
        break
    else:
        print("Invalid Choice! select(1,2,3,4)")