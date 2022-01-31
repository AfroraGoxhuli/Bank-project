from Account import Account
from Customer import Customer 

class Datasource:
    

    def addInfoToFile (self,allCustomers):
        with open("file_customerInfo.txt", mode= "wt") as file:
            insert_text= ""
            for customer in allCustomers:
                insert_text += f"{customer.get_customer_id()}:{customer.get_name()}:{customer._last_name}:"f"{customer.get_ssn()}"
                for account in customer.get_account():
                    insert_text += f"#{account.get_account_number()}:{account.get_account_type()}" f":{account.get_account_balance()} "
                insert_text += "\n"
            file.write(insert_text)

    def getLastId(self):
        list_id = []
        with open("customerInfo.txt", mode="rt") as file:
            for line in file:
                string_split = line.strip().split(":")
                list_id.append(string_split[0])
                last_id = list_id[-1]
        return last_id

    def getLastAccountNumber(self):
        list_id = []
        with open("customerInfo.txt", mode="rt") as file:
            for line in file:
                first_split = line.strip().split("#")
                for index, middlehand in enumerate(first_split):
                    if not index == 0:
                        account_elements = middlehand.split(":")
                        list_id.append(account_elements[0])
        return max(list_id)

    def getInfoFromTextFile(self):

        with open("customerInfo.txt", mode="rt") as file:
            temp = file.read()
            data_as_string = temp.split("\n")
            customers = []
        if not data_as_string[-1]:
            data_as_string.pop()

        for line in data_as_string:
            accounts = []
            first_split = line.split("#")

            for index, second_split in enumerate(first_split):
                element = second_split.split(":")
                if index == 0:
                    customer_id = element[0]
                    name = element[1]
                    last_name = element[2]
                    ssn = element[3]
                else:
                    account_number = element[0]
                    account_type = element[1]
                    account_balance = element[2]
                    accounts.append(Account(account_number, account_type, account_balance))
            customers.append(Customer(customer_id, name, last_name, ssn, accounts))
        return customers
