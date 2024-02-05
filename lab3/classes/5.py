class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, num):
        self.balance += num
        print(self.balance)
    
    def withdraw(self, num):
        if self.balance < num:
            print("Error")
        else:
            self.balance -= num
            print(self.balance)
    
acc = Account("Danial", 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.withdraw(9000)
