class Bank:
    def __init__(self, acctno, bal, ifsc, name,pin):
        self.acctno = acctno
        self.bal = bal
        self.ifsc = ifsc
        self.name = name 
        self.pin = pin
    
    def display(self):
        print(self.name,self.acctno,self.bal)
        
act = Bank(1,3000,'abc1','naresh',123)
act.display()
    
