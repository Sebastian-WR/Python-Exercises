class Bank:
    def __init__(self, bankName, address):
        self.bankName = bankName
        self.address = address
        self.accounts = []
    
    def toString(self):
        print(str(Sparnord.__dict__) +  " " + str(self.accounts) + "\n" + str(self.accounts[1].customer.name))

class Account:
    def __init__(self, accNumber, dough, customer):
        self.accNumber = accNumber
        self.dough = dough
        self.customer = customer

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

Sparnord = Bank('Sparnord', 'Hjørring')
AnneLise = Customer('Anne-Lise', 'AL@lol.dk')
ALAcc = Account(1, 3000, AnneLise)
Lars = Customer('Lars', 'Lars@email.dk')
ALars = Account(2, 5000, Lars)
Sparnord.accounts.append(ALAcc)
Sparnord.accounts.append(ALars)
Sparnord.toString()

