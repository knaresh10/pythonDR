class Bank:
    def __init__(self, acctno, bal, ifsc, name,pin):
        self.acctno = acctno
        self.bal = bal
        self.ifsc = ifsc
        self.name = name 
        self.pin = pin
    
    def withdraw(self, amt):
        if(self.bal >= amt):
            print("Amount is taken")
            self.bal -= amt 
        else:
            print("insufficient balance")

#__Main____
act = Bank(1,3000,'abc1','naresh',123)
act.withdraw(1000)
    