# Initialize account details for multiple users
accounts = {
    "user1": {"account_number": "123456789", "pin": "1234", "balance": 1000, "transaction_history": []},
    "user2": {"account_number": "987654321", "pin": "4321", "balance": 500, "transaction_history": []}
}

# Function to display the main menu
def display_menu():
    print("Welcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

# Function to authenticate user
def authenticate():
    entered_account_number = input("Enter your account number: ")
    entered_pin = input("Enter your PIN: ")
    for user, details in accounts.items():
        if details['account_number'] == entered_account_number and details['pin'] == entered_pin:
            return user, details
    return None, None

# Function to check balance 
def check_balance(user, details):
    print(f"Your current balance is: £{details['balance']}")

# Function to deposit money
def deposit_money(user, details):
    amount = float(input("Enter amount to deposit: £"))
    details['balance'] += amount  # Add the deposit amount to balance
    details['transaction_history'].append(f"Deposited: £{amount}")  # Record the transaction
    print(f"You have deposited: £{amount}")
    check_balance(user, details)  # Show updated balance

# Function to withdraw money
def withdraw_money(user, details):
    amount = float(input("Enter amount to withdraw: £"))
    if amount > details['balance']:
        print("Insufficient funds!")
    else:
        details['balance'] -= amount  # Subtract the withdrawal amount from balance
        details['transaction_history'].append(f"Withdrew: £{amount}")  # Record the transaction
        print(f"You have withdrawn: £{amount}")
        check_balance(user, details)  # Show updated balance

# Function to view transaction history
def view_transaction_history(details):
    if details['transaction_history']:
        print("Transaction History:")
        for transaction in details['transaction_history']:
            print(transaction)
    else:
        print("No transactions found.")

# Main program loop
def main():
    while True:
        user, details = authenticate()
        if user:
            while True:
                display_menu()
                choice = input("Select an option: ")
                if choice == '1':
                    check_balance(user, details)
                elif choice == '2':
                    deposit_money(user, details)
                elif choice == '3':
                    withdraw_money(user, details)
                elif choice == '4':
                    view_transaction_history(details)
                elif choice == '5':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Authentication failed. Please try again.")

# Run the program
main()

