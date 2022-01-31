from Account import Account

class Customer():
    def __init__(self,customer_id,first_name,last_name,ssn,accounts,transaction):
        self.customer_id = customer_id
        self.first_name = ""
        self.lastName = ""
        self.ssn = ssn
        self.accounts = []
        self.transactions = []
    
    def __str__(self):
        return f"ID: {self.customer_id}\nName: {self.first_name}\nLastname: {self.last_name}\nSSN: {self.ssn}"

    
    def show_details(self):
        print ('customer_id', self.customer_id)
        print ('first_name', self.first_name)
        print ('last_name', self.last_name)
        print ('ssn', self.ssn)
        print ('accounts', self.accounts)
        print ('transaction', self.transactions)

    def get_ssn (self):
        return self.ssn 
    
    def get_name (self):
        return self.first_name, self.last_name
    
    def get_customer_id( self):
        return self.customer_id

    def get_account(self):
        return self.accounts

    def set_name (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name