# Create a Account class with 2 attributes - balance & account no. Create method for debit,credit & printing the balance.

class Account():
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc

    def debit(self,amount):
        self.balance = self.balance - amount
        print("Rs.",amount,"was debited")
        print("total balnce = ",self.balance)

    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs.",amount,"was credited")
        print("total balnce = ",self.balance)
    def get_balance(self):
        return self.balance

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(600)





    