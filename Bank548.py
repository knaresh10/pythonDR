import random as r
class Swiss():
    def __init__(self, ac_no, ifsc, name, pin):
        self.ac_no=ac_no
        self.ifsc=ifsc
        self.name=name
        self.bal=r.randint(100000000,10000000000000)
        self.pin=pin
        
    def wd(self,x):
        if self.bal<x:
            print("\tOut of balance")
        else:
            print("Enter PIN")
            i=input()
            print(self.pin,' ',i)
            if i==self.pin:
                print("\tTransaction successful")
                print("your current balance: ",self.bal-x)
            else:
                print("\tInvalid PIN")

    def deposit(self,x):
        print("deposit successful")
        self.bal+=x
        print("\tyour current balance: ",self.bal)

    def checkpin(self,x):
        if x==self.pin:
            print("\tVALID PIN")
        else:
            print("\tINVALID PIN")
    def changepin(self,x):
        x1=input("Enter your current PIN")
        if x==self.pin:
            self.pin=x
            print("your pin changed to: ",x)
        else:
            print("\tINVALID PIN")

print('''Welcome to Swiss bank\n\tPlease Enter:''')
ac=int(input('-->account No.:'))
iff=input('-->IFSC.:')
nn=input('-->your Name: ')
pp=input('-->Enter PIN: ')
ob=Swiss(ac,iff,nn,pp)
print('\tGreeting ',nn)
print('\tENTER following')
n=True
while(n):
    print("1 : withdraw")
    print("2 : deposit")
    print("3 : checkpin")
    print("4 : change")
    print("0 : EXIT")
    n=int(input())
    if(n==1):
        print("Enter amount:")
        n1=int(input())
        ob.wd(n1)
    elif(n==2):
        print("Enter amount:")
        n1=int(input())
        ob.deposit(n1)
    elif(n==3):
        print("Enter PIN:")
        n1=input()
        ob.checkpin(n1)
    elif(n==4):
        print("Enter PIN:")
        n1=input()
        ob.changepin(n1)
    elif(n==0):
        print('''Thanks for Visitng
    Have a Nice Day!''')
    else:
        print('''Enter valid option
        Try Again!''')
