import random
import time
class Bank:
    def __init__(self,actno, name,pin):
        self.accoutNumber = actno
        self.balance = 0
        self.ifsccode = 'ACET2024'
        self.name = name 
        self.pin = pin 
    
    def display(self):
        print("Your name : ",self.name)
        print("Your account number : ",self.accoutNumber)
        print("Your IFSC Code : ",self.ifsccode)
        print("Your current balance : ", self.balance)
    def withdraw(self):
        pin =  input("Enter your pin : ")
        if pin != self.pin:
            print("Wrong pin try again")
        else:
            amount = int(input("Enter amount you want to withdraw : "))
            if self.balance < amount :
                print("Insufficient amount")
                print("your balance is ",self.balance)
            else:
                self.balance -= amount
                print("Collect your ",amount)
                print("Remaining balance : ",self.balance)
    
    def deposit(self):
        pin =  input("Enter your pin : ")
        if pin != self.pin:
            print("Wrong pin try again")
        else:
            amount = int(input("Enter amount you want to deposit : "))
            self.balance += amount 
    
    def checkBalance(self):
        pin = input("Enter your pin : ")
        if pin != self.pin:
            print("Please check your pin")
        else:
            print("Your current balance is ", self.balance)
    
    def changePin(self):
        pin = input("Enter your pin : ")
        if pin != self.pin:
            print("Entered wrong pin")
        else:
            self.pin = input("Enter your new pin: ")


#__MAIN___
name = input("Enter you name : ")
accountNo = '2024'+str(random.randint(100000, 999999))
pin = input("Enter your desired 4 numbered pin :")

obj = Bank(accountNo, name, pin)
obj.display()
while True:
    print("""Enter 1 to deposit money
Enter 2 to withdraw money
Enter 3 to check balance
Enter 4 to change pin number
Enter 5 to stop""")
    n = int(input("Your option : "))
    if n == 1:
        obj.deposit()
    elif n == 2:
        obj.withdraw()
    elif n == 3:
        obj.checkBalance()
    elif n == 4:
        obj.changePin()
    elif n == 5:
        print("Thanks for using our service")
        break 
    else:
        print("invalid option")
    time.sleep(2)