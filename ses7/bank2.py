class Bank:
    def __init__(self, accounts):
        self.accounts = []
        self.accounts.append(accounts)
    
    @property
    def accounts(self):
        return self.accounts
    
    @accounts.setter
    def accounts(self, accounts):
        self.accounts.append(accounts)

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

    @property
    def no(self):
        return self.__no

    @no.setter
    def no(self, no):
        self.__no = no
    
    @property
    def cust(self):
        return self.__cust

    @cust.setter
    def cust(self, cust):
        self.__cust = cust

class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

cust1 = Customer("Chris")
acc1 = Account(1, cust1)
Sparnord = Bank(acc1)
