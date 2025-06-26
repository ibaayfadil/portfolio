class bankAccount:
    def __init__(self, name, saldo):
        self.name = name
        self.saldo = saldo
    
    def userName(self):
        print(self.name)
    
    def userBalance(self):
        print(self.saldo)
    
    def userDeposit(self, deposit):
        self.saldo = deposit + self.saldo
        print("Deposit berhasil dilakukan, jumlah saldo sekarang",self.saldo)
        
    
    def userWithdraw(self, out):
        if self.saldo >= out:
            self.saldo -= out
            print("penarikan berhasil sisa saldo ", self.saldo)
        else:
            print("saldo tidak mencukupi, saldo anda saat ini", self.saldo)
       
    
user1 = bankAccount('Iqbal', 750)
user1.userName()
user1.userBalance()
user1.userDeposit(100)
user1.userWithdraw(850)
