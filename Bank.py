from Datasource import Datasource
from Customer import Customer
from Account import Account

class Bank:
    
    def __init__(self):
        self.allCustomers = []
        self.data_store = Datasource()
        self._load()

    def _load(self):
        self.allCustomers = self.data_store.getInfoFromTextFile()

    def get_customers(self):
        for customer in self.allCustomers:
            print (customer)
    
    def addCustomer(self, first_name, last_name, ssn):
        last_id = int(self.data_info.getLastId())
        last_id += 1
        for customer in self.allCustomers:
            if ssn == customer.get_ssn():
                return "Customer already exists"
        new_customer = Customer(last_id, first_name, last_name, ssn, [])
        self.allCustomers.append(new_customer)
        self.data_store.addInfoToFile(self.allCustomers)
        return "New Customer has been added!"

    def change_customer_name(self, first_name,last_name, ssn):
        for customer in self.allCustomers:
            if ssn == customer.get_ssn():
                customer.set_firstName(first_name, last_name)
            self.data_store.addInfoToFile(self.allCustomers)

    def remove_customer(self, ssn):
        for customer in self.allCustomers:
            if customer.get_ssn() == ssn:
                index = self.allCustomers.index(customer)
                self.allCustomers.pop(index)
        self.data_store.addInfoToFile(self.allCustomers)

    def add_account(self, ssn):
            last_account_number = int(self.data_store.getLastAccountNumber())
            last_account_number += 1
            for customer in self.allCustomers:
                if customer.get_ssn() == ssn:
                    new_account = Account(new_account, "debit", 0.0)
                customer.get_account().append(new_account)
            self.data_store.addInfoToFile(self.allCustomers)

    def get_account(self, ssn, account_number):
            for customer in self.allCustomers:
                if ssn == customer.get_ssn():
                    for account in customer.get_account():
                        if account_number == account.get_account_number():
                            print(account)

    def deposit(self, amount, balance):
            self.amount = amount
            self.balance = self.balance + amount
            print ("Account balance has been updated : kr", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if  self.amount > self.balance:
            print("Not enough money | Balance available : kr", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance had been updated: kr", self.balance)

   
