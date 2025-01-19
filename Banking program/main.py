def show_balance(balance):
    print(f"Your current balance is: ${balance}")

def deposit_money():
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        return 0
    else:
        return amount

def withdraw_money(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        return 0
    elif amount > balance:
        print("Insufficient funds. Please deposit more money.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit_money()
        elif choice == 3:
            balance -= withdraw_money(balance)
        elif choice == 4:
            is_running = False
            print("Thank you for using our ATM. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using our ATM. Goodbye!")

if __name__ == "__main__":
    main()
