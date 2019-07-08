class Account(Counter):
    def __init__(self, holder, number, balance, credit_line=1500):
        Counter.__init__(self)
        self.__Holder = holder
        self.__Number = number
        self.__Balance = balance
        self.__CreditLine = credit_line

    def deposit(self, amount):
        self.Balance = amount
    def widthraw(self, amount):
        if(self.Balance - amount  < -self.CreditLine):
            #coverage insufficient
            return False
        else:
            self.Balance -= amount
            return True
    def balance(self):
        return self.Balance
    def transfer(self, target, amount):
        if(self.Balance - amount < -self.CreditLine):
            #coverage insufficient
            return False
        else:
            self.Balance -= amount
            target.Balance += amount
            return True
        
        
