class BankAccount:
  def __init__(self,balance):
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    
  def withdraw(self, amount):
    if(amount > self.balance):
      return "invalid transaction"
    else:
      self.balance -= amount

class MinimumBalanceAccount(BankAccount):
    def __init__(self,balance):
        self.balance = balance

#another way to implement it
##class BankAccount:
##    def __init__(self,balance=0):
##        self.balance = balance
##
##    def deposit(self, deposit_amount=30):
##        self.deposit_amount=deposit_amount
##        self.balance += deposit_amount
##        return self.balance
##
##    def withdraw(self,withdraw_amount=10):
##        if withdraw_amount > self.balance:
##            raise RuntimeError('Invalid Transaction')
##        self.balance -= withdraw_amount
##        return self.balance
##
##class MinimumBalanceAccount(BankAccount):
##    def __init__(self,balance = 0):
##        self.balance = balance
