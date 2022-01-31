from Bank import Bank


class Menu:

    def __init__(self):
        self.bank = Bank()
        self.menuOptions()

    def menuOptions(self):
        option = -1
        while option != 0:
            self.menu()
            option = input("What do you want to do today? Choose option")
            if option == "1":
                self.bank.getCustomers()
            elif option == "2":
                first_name = input("Firstname: ")
                last_name = input("Lastname: ")
                ssn = input("SSN: ")
                print(self.bank.addCustomer(first_name, last_name, ssn))
            elif option == "3":
                ssn = input("SSN: ")
                self.bank.getCustomer(ssn)
            elif option == "4":
                first_name = input("Firstname: ")
                last_name = input("Lastname: ")
                ssn = input("SSN: ")
                self.bank.changeCustomerName(first_name, last_name, ssn)
            elif option == "5":
                ssn = input("SSN: ")
                self.bank.removeCustomer(ssn)
            elif option == "6":
                ssn = input("SSN: ")
                self.bank.addAccount(ssn)
            elif option == "7":
                ssn = input("SSN: ")
                account_number = input("Account number: ")
                self.bank.getAccount(ssn, account_number)
            elif option == "8":
                ssn = input("SSN: ")
                account_number = input("Account number:")
                self.bank.removeAccount(ssn, account_number)
            elif option == "9":
                ssn = input("SSN: ")
                account_number = input("Account number: ")
                amount = input("Amount: ")
                self.bank.deposit(ssn, account_number, amount)
            elif option == "10":
                ssn = input("SSN: ")
                account_number = input("Account number: ")
                amount = input("Amount: ")
                print(self.bank.withdraw(ssn, account_number, amount))
            elif option == "0":
                print("Thank You and welcome back")
            else:
                print("Option invalid")

    def menu(self):
        print("|" + 50 * "-" + "|")
        print(" Bank:")
        print(" 1. Show all customers.")
        print(" 2. Add a new customer.")
        print(" 3. Get a specific customer.")
        print(" 4. Change customer name.")
        print(" 5. Remove a customer.")
        print(" 6. Add a new account for customer.")
        print(" 7. Get account information for a customer.")
        print(" 8. Remove an account for customer.")
        print(" 9. Deposit.")
        print(" 10. Withdraw.")
        print("|" + 50 * "-" + "|")