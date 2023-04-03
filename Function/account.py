class BankAccount():
    
    def __init__(self, number, balance, name):
        # 동일계좌번호 여부 체크
        self.account_number = number
        self.account_balance = balance
        self.account_holder_name = name

    def __str__(self):
       return 'account name    : ' + str(self.account_holder_name) + '\naccount number  : ' + str(self.account_number) + '\naccount balance : ' + str(self.account_balance)


    def get_account_number(self):
        return self.account_number
    

    def get_account_balance(self):
        return self.account_balance
    

    def get_account_holder_name(self):
        return self.account_holder_name   
    
    
    def get_account_info(self):
        return self

    def deposit(self, amount):
        if amount <= 0:
           print('Error : Invaild deposit amount')
           return
        
        self.account_balance += amount
        print(amount, 'deposited to', self.account_number)
    

    def withdraw(self, amount):
        if amount > self.account_balance:
           print('Error : Invaild withdraw amount')
           return
        
        self.account_balance -= amount
        print(amount, 'withdraw from', self.account_number)

    
    



account1 = BankAccount('1234567890', 5000, 'Jone Doe')
account1.deposit(1000)
print(account1.get_account_info())
account1.withdraw(2000)