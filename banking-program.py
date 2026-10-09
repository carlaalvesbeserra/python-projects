# Banking Program

def show_balance(balance):
    print(f"Your current balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter your deposit amount: "))

    if amount < 0:
        print("That is not a valid amount.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter your withdraw amount: "))

    if amount < 0:
        print("Amount cannot be negative.")
        return 0
    elif amount > balance:
        print("Insufficient fund.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    print("*****************")
    print("Banking Program")
    print("*****************")

    while is_running:
        print("*****************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*****************")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("That is not a valid choice.")
            print("Please select a number between 1 and 4")

    print("*********************************")
    print("Thank you for using this program")
    print("*********************************")

if __name__ == "__main__":
    main()