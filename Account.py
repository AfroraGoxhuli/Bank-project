class Account():
    def __init__(self,customer_id,account_number, account_type,balance, amount):
        self.customer_id = customer_id
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Accountnumber: {self.account_number}\nAccounttype: {self.account_type}\nAccountbalance: {self.balance}"

    def add_money (self, amount):
        self.balance += amount
        return self.amount
    
    def withdraw_money (self, amount):
        self.balance -= amount
        return self.amount
    
    def get_account (self, account_number):
        return self.account_number 
    
    def show_accountinfo (self):
        return "\nCustomer:" + self.customer_id + "\nAccount number and type:" + self.account_number + self.account_type + "\nBalance:" + self.balance