class ATM:
    def _init_(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You deposited ${amount}. New balance is: ${self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"You withdrew ${amount}. New balance is: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            print("Invalid withdrawal amount")

    def pinchange(self,pin,account):
        if pin==1007 and account==1234567890:
            self.newpin=int(input("Enter new pin:"))
            print("Your new pin is:",self.newpin)

    def exit(self):
        print("Thank you for using the ATM. Goodbye!")


def atm_menu():
    atm = ATM(balance=1000)  # Initial balance can be set here
    pin=int(input("Enter the pin:"))
    account=int(input("Enter the pin:"))
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4.PIN Change")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            atm.pinchange(pin,account)
        elif choice == '5':
            atm.exit()
            break
        else:
            print("Invalid choice! Please try again.")



atm_menu()