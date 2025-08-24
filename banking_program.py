#Show users current balance
def show_balance(balance):
    print("*******************")
    print(f"Your balance is ${balance:.2f}")
    print("*******************")

#Prompts the user for amout to be deposited
def deposit():
    print("*******************")
    try:
        amount=float(input("Enter an amount to be deposited: "))
    except:
        print("Invalid Input")
        return 0
    print("*******************")
    if amount<0:
        print("*******************")
        print("That's not a valid amount")
        print("*******************")
        return 0
    else:
        return amount
    
#Prompts the user for amout to be taken out
def withdraw(balance):
    print("*******************")
    try:
        amount=float(input("Enter amount to be withdrawn: "))
    except:
        print("Invalid Input")
        return 0
    print("*******************")

    if amount>balance:
        print("*******************")
        print("Insufficient funds")
        print("*******************")
        return 0
    elif amount<0:
        print("*******************")
        print("Amount must be greater than 0")
        print("*******************")
        return 0
    else:
        print(f"Amount: {amount:.2f} withrawn successfully")
        return amount

#entry point of the program
def main():
    balance=0
    is_running=True

    while is_running:
        print("*******************")
        print("  Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*******************")
        try:
            choice=input("Enter you choice (1-4): ")
        except:
            print("Invalid Input")

        if choice=='1':
            show_balance(balance)
        elif choice =='2':
            balance+=deposit()
        elif choice == '3':
            balance-=withdraw(balance)
        elif choice == '4':
            is_running=False
        else:
            print("This is not a valid choice")
    print("*******************")
    print("Thank you have a nice day.")
    print("*******************")

#envoke the main method
main()

