class Checking_Account:
    def __init__(self,name,accnum,addy,balance):
        self.name = name
        self.accnum = accnum
        self.addy = addy
        self.__balance = balance
    
    def get_account_name(self):
        return self.name
    
    def get_accnum(self):
        return self.accnum
    
    def get_addy(self):
        return self.addy
    
    def get_balance (self):
        balance_copy = self.__balance
        return balance_copy
    
    def debit (self,amount):
        if(self.__balance-amount<0):
            return 0
        else:
            self.__balance -=amount
            return 1
        
    def credit (self,amount):
        self.__balance+=amount
        return 1
        
    